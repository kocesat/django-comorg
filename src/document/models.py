from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name= 'subfolders', blank=True, null=True)

    def __str__(self):
        return self.name


class File(models.Model):    
    name = models.CharField(max_length=140)
    description = models.TextField(max_length=250, blank=True, null=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    icon = models.ImageField(default='images/no_img.png', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.name
