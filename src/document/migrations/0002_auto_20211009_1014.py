# Generated by Django 3.1.7 on 2021-10-09 07:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='icon',
            field=models.ImageField(default='images/no_img.png', upload_to=''),
        ),
    ]
