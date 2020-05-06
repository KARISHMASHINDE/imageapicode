from django.contrib import admin
from django.db import models
from .models import apiuser,imageprofile

# Register your models here.

admin.site.register(apiuser)
admin.site.register(imageprofile)