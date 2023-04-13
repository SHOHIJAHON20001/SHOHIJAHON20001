from django.contrib import admin
from django.contrib.auth.models import Group, User
from myapp.models import SotibOlish

# Register your models here.

admin.site.unregister([Group, User])
admin.site.register([SotibOlish])
