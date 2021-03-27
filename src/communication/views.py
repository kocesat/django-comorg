from django.shortcuts import render, redirect, get_object_or_404
from .models import Broadcast
from .forms import BroadcastCreateForm
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from comorg.settings import EMAIL_HOST_USER


User = get_user_model()


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
def list_unpublished(request):
    # get only unpublished broadcast
    broadcasts = Broadcast.objects.filter(is_published=False)
    return render(
        request,
        'communication/broadcast/unpublished.html',
        {
            'broadcasts': broadcasts
        }
    )


@login_required
def new_broadcast(request):
    if request.method == 'POST':
        form = BroadcastCreateForm(request.POST)
        if form.is_valid():
            broadcast = form.save(commit=False)
            broadcast.user = request.user
            broadcast.save()
            if broadcast.is_published:
                broadcast.published = now()
                users = User.objects.filter(is_active=True)
                # TODO send_mail as async via Celery worker
                send_mail(
                    subject='[Test]Comorg System Broadcast',
                    message=
                    'A new broadcast was published.Check out the Comorg Portal to see the details\n'
                    f'Subject: {broadcast.title} \n'
                    'Good day, \n'
                    'Comorg System Administration',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=users,
                    fail_silently=False
                )
                messages.success(request, 'Published successfully')
            else:
                messages.success(request, 'Saved successfully')
            return redirect('communication:broadcast_list')
    else:
        form = BroadcastCreateForm()
    return render(request, 'communication/broadcast/new.html', {'form': form})


def publish(request, broadcast_id):
    # find the broadcast from database
    broadcast = get_object_or_404(Broadcast, id=broadcast_id)
    if broadcast.is_published:
        messages.error(request, "Already published")
        return redirect('communication:broadcast_list')
    elif not broadcast.is_published and request.user.has_perm('communication.change_broadcast'):
        broadcast.publish()
        broadcast.save()
        # send email to users
        users = User.objects.filter(is_active=True)
        # TODO send_mail as async via Celery worker
        send_mail(
            subject='[Test]Comorg System Broadcast',
            message=
            'A new broadcast was published.Check out the Comorg Portal to see the details\n'
            f'Subject: {broadcast.title} \n'
            'Good day, \n'
            'Comorg System Administration',
            from_email=EMAIL_HOST_USER,
            recipient_list=users,
            fail_silently=False
        )
        messages.success(request, 'Published succesfully')
        return redirect('communication:list_unpublished')
    else:
        messages.error(request, 'Unauthorized action')
        return redirect('communication:list_unpublished')


@login_required
def unpublish(request, broadcast_id):
    broadcast = get_object_or_404(Broadcast, id=broadcast_id)
    if not broadcast.is_published: 
        messages.error(request, "Already unpublished")
        return redirect('communication:list_unpublished')
    elif broadcast.is_published and request.user.has_perm('communication.change_broadcast'):
        broadcast.unpublish()
        broadcast.save()
        messages.success(request, "Unpublished successfully")
        return redirect('communication:broadcast_list')
    else:
        messages.error(request, 'Unauthorized action')
        return redirect('communication:broadcast_list')

