from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from djongo import models
import jsonfield
from django.db.models import BigAutoField
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

import json

class DecisionTable(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    element = models.CharField(_("Element"), max_length=20)
    priority = models.IntegerField(_("Priority"))
    # parent = models.CharField(_("Parent"), max_length=100)
    title = models.CharField(_("Title"), max_length=50)

    def __str__(self):
        return self.title

class BookContent(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    docId = models.CharField(
        _("Google Doc ID"), max_length=100)
    revisionCode = models.CharField(
        null=True, default='', blank=True, max_length=100)
    content = jsonfield.JSONField(
        _("Book Content (JSON)"), null=True, default={}, blank=True)
    # contentfield = models.TextField(
    #     _("Book Content (JSON)"), null=True, default="", blank=True)
    book = models.ForeignKey(
        'book.Book', blank=True, null=True, on_delete=models.CASCADE, related_name='book_content_meta')
    revision = models.ForeignKey(
        'book.BookRevision', blank=True, null=True, on_delete=models.CASCADE, related_name='book_content_revision')
    modifiedBy = models.ForeignKey(
        "authorization.User", default=1, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return f'{self.id}'

    @property
    def _id(self):
        return str(self._id)

    


class BookRevision(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=30, blank=True,)
    author = models.CharField(_("Author"), max_length=30, blank=True,)
    publisher = models.CharField(_("Publisher"), max_length=30, blank=True,)
    book = models.ForeignKey(
        'book.Book', blank=True, null=True, on_delete=models.CASCADE, related_name='book_revision_meta')
    content = models.ForeignKey(
        'book.BookContent' ,null=True, blank=True, on_delete=models.CASCADE, related_name='book_revision_content', default=None)
    modifiedBy = models.ForeignKey(
        "authorization.User", default=1, on_delete=models.CASCADE)
    isPublished = models.BooleanField(default=False)
    createdAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.id})'

    @property
    def _id(self):
        return str(self._id)

    @property
    def book(self):
        if self.content:
            return self.content.content
        else:
            return None

    @property
    def revisionCode(self):
        if self.content:
            return self.content.revisionCode
        else:
            return None

    @property
    def googleDoc(self):
        if self.content:
            return self.content.docId
        else:
            return None


class Book(models.Model):
    id = models.UUIDField(_("UUID"), default=uuid.uuid4,
                          primary_key=True, editable=False)
    isPublished = models.BooleanField(default=False)
    latest = models.ForeignKey(
        "book.BookRevision", default=None, on_delete=models.CASCADE, blank=True, null=True, related_name='book_content')
    modifiedBy = models.ForeignKey(
        "authorization.User", default=1, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return f'{self.id}'

    @property
    def _id(self):
        return str(self._id)

    @property
    def title(self):
        if self.latest:
            return str(self.latest.title)
        else:
            return str("Book Title")

    @property
    def publisher(self):
        if self.latest:
            return str(self.latest.publisher)
        else:
            return str("Publisher Name")

    @property
    def author(self):
        if self.latest:
            return str(self.latest.author)
        else:
            return str("Author Name")

    @property
    def revisionPublished(self):
        if self.latest:
            return self.latest.isPublished
        else:
            return False

    @property
    def book(self):
        if self.latest:
            return self.latest.book
        else:
            return None

    @property
    def revisionCode(self):
        if self.latest:
            return self.latest.revisionCode
        else:
            return None

    @property
    def googleDoc(self):
        if self.latest:
            return self.latest.docId
        else:
            return None


@receiver(post_save, sender=BookContent, dispatch_uid="update_book_content")
def update_content(sender, instance, created, **kwargs):
    if created:
        if instance.revision:
            try:
                bookRevision = BookRevision.objects.get(id=instance.revision_id)
                bookRevision.content_id = instance.id
                bookRevision.save()
                return
            except BookContent.DoesNotExist:
                pass
        
        bookRevision=BookRevision.objects.create(content=instance,modifiedBy=instance.modifiedBy)
        instance.revision_id=bookRevision.id
        instance.save()


import json
import requests

@receiver(post_save, sender=BookContent, dispatch_uid="convert_to_json")
def convert(sender, instance, created, **kwargs):
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
    SERVICE_ACCOUNT_FILE = 'staticfiles/book/js/keys.json'

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SCOPES = ['https://www.googleapis.com/auth/documents']
    
    DOCUMENT_ID = instance.docId
    service = build('docs', 'v1', credentials=creds)

    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    values= document.get('body',[])
    
    res = requests.get(str(values))
 
    # Convert data to dict
    data = json.loads(res.text)
 
    # Convert dict to string
    data = json.dumps(data)
    
    print(data)
    print(type(data))


    if created:
        instance.content=values
        instance.save()

