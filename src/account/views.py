from django.shortcuts import render
from .models import Participant, User


def account_list(request):
    users = User.objects.select_related('participant').all()
    
    return render(request, 'account/users/list.html', {
        'users': users
    })

def participant_list(request):
    participants = Participant.objects.all()
    
    return render(
        request,
        'account/participants/list.html',
        {
            'participants': participants
        }
    )