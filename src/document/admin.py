from django.contrib import admin
from .models import File, Folder

# Register your models here.
admin.site.register(Folder)
admin.site.register(File)