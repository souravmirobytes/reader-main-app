from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    fullName = models.CharField(
        _("Full Name"), max_length=100, default='', null=False, blank=True)
    phoneNumber = PhoneNumberField(_("Phone Number"))
    email = models.EmailField(_("Email ID"), max_length=254)
    password = models.CharField(_("Encrypted Password"), max_length=30)
    createdAt = models.DateTimeField(_("Created At"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return f'{self.fullName} ({self.id})'

    @property
    def _id(self):
        return str(self._id)
