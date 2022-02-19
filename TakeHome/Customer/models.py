from django.db import models
from user.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save


class Customer(models.Model):
    
    # is_customer = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass

    
    

    

    