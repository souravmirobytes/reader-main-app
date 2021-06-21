from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from djongo import models
from django.db.models import BigAutoField
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver


class BookContent(models.Model):
    id = models.UUIDField(_("UUID"), primary_key=True,
                          default=uuid.uuid4, editable=False)
    docId = models.CharField(
        _("Google Doc ID"), max_length=100, null=True, default='', blank=True)
    revisionCode = models.CharField(
        null=True, default='', blank=True, max_length=100)
    # content = models.JSONField(
    #     _("Book Content (JSON)"), null=True, default=None, blank=True)
    contentfield = models.TextField(
        _("Book Content (JSON)"), null=True, default="", blank=True)
    book = models.ForeignKey(
        'book.Book', blank=True, null=True, on_delete=models.CASCADE, related_name='book_content_meta')
    revision = models.ForeignKey(
        'book.BookRevision', blank=True, null=True,unique=True, on_delete=models.CASCADE, related_name='book_content_revision')
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
        'book.BookContent' ,null=True, blank=True,unique=True, on_delete=models.CASCADE, related_name='book_revision_content', default=None)
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


@receiver(post_save, sender=BookRevision, dispatch_uid="update_book_content")
def update_content(sender, instance,created, **kwargs):
    # if instance.revision:
    #     try:
    #         bookRevision = BookRevision.objects.get(id=instance.revision)
    #         bookRevision.content = instance.id
    #         bookRevision.save()
    #         return
    #     except BookContent.DoesNotExist:
    #         pass
    
    # bookRevision=BookRevision.objects.create(book=instance.book,content=instance.id,modifiedBy=instance.modifiedBy)
    # instance.revision=bookRevision.id
    # instance.save()
    if created:
        obj=BookContent.objects.filter(id=instance.content).exists()
        obj.revision = instance.id
        obj.revision.save()
    abcd