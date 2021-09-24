from django.contrib import admin
from .models import Category, File, Folder

# Register your models here.
admin.site.register(Category)
admin.site.register(Folder)
admin.site.register(File)