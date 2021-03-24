from django import forms
from .models import Broadcast


class BroadcastCreateForm(forms.ModelForm):

    class Meta:
        model = Broadcast
        fields = ['title', 'body', 'is_published']