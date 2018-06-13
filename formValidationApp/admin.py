from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
# this will register the model in django-admin section and we could see/change our data there
