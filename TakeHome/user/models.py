from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    name = models.CharField(_('Name'), max_length=30, null=True, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    #added is_customer flag
    is_customer = models.BooleanField(default=True)
    objects = managers.UserManager()
    
    #changed to name for basic auth
    USERNAME_FIELD = 'name'
    #REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.name
