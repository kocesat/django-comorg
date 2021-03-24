from django.shortcuts import render, redirect
from .models import Broadcast
from .forms import BroadcastCreateForm
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    # get only published broadcast
    broadcasts = Broadcast.objects.filter(is_published=True)
    return render(
        request, 
        'communication/broadcast/list.html',
        {
            'broadcasts': broadcasts
        })

@login_required
def new_broadcast(request):
    if request.method == 'POST':
        form = BroadcastCreateForm(request.POST)
        if form.is_valid():
            broadcast = form.save(commit=False)
            broadcast.published = now()
            broadcast.user = request.user
            broadcast.save()
            if broadcast.is_published:
                messages.success(request, 'Published successfully')
            else:
                messages.success(request, 'Saved successfully')
            return redirect('communication:broadcast_list')
    else:
        form = BroadcastCreateForm()
    return render(request, 'communication/broadcast/new.html', {'form': form})
