from django.contrib import admin
from Customer.models import Customer
from user.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register([Customer,User])

@admin.register
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username', 'email', 'is_active'
    )

