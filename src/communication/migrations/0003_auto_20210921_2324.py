# Generated by Django 3.1.7 on 2021-09-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_auto_20210325_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Publish immediately'),
        ),
    ]
