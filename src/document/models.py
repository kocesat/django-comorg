from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=140)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='folders')
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name= 'subfolders', blank=True, null=True)

    def __str__(self):
        return self.name


class File(models.Model):    
    name = models.CharField(max_length=140)
    description = models.TextField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.name
