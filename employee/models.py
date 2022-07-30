import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext as _


class AbstructBaseModel(models.Model):
    '''
    Base model to inherit in rest models
    id: UUID field(unique)
    created_at: Date time field default is current timestamp
    updated_at: Date time field default is current timestamp
    '''
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))


class User(AbstractUser):
    '''
    User model to add fields in default user model
    id: UUID field(unique)
    email: User/Employee email
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        if self.first_name is None or self.first_name == "":
            self.first_name = self.username
        if self.last_name is None or self.last_name == "":
            self.last_name = ""
        return "{} {}".format(self.first_name, self.last_name)

    objects = UserManager()
