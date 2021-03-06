# Generated by Django 3.1.7 on 2021-03-24 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadcast',
            options={'ordering': ['-published']},
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='broadcasts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='broadcast',
            table='broadcasts',
        ),
    ]
