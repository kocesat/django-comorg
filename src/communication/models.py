from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Broadcast(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='broadcasts')
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)  # TODO: Add rich text widget here
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name='Publish immediately')

    class Meta:
        db_table = 'broadcasts'
        ordering = ['-published']

    def publish(self):
        self.is_published = True
        self.published = timezone.now()

    def unpublish(self):
        self.is_published = False 

    def __str__(self):
        return f'{self.title} published at {self.published}'


