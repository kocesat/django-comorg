from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant, User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import (
    UserRegistrationForm, 
    UserEditForm) 


def account_list(request):
    users = User.objects.select_related('participant').all()
    print(users[0].groups.values_list('name', flat=True).first())    
    return render(request, 'account/users/list.html', {
        'users': users,
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

@login_required
# @permission_required('account.can_activate_user', raise_exception=True)
def activate_user(request, user_id: int):
    if request.user.has_perm('account.can_activate_user') == False:
        messages.error(request, 'Unauthorized action')
        return redirect('account:account_list')
    user_to_be_activated = get_object_or_404(User, id=user_id)
    # check if the activating user is in the same organization as the activated user
    if request.user.is_superuser or request.user.participant == user_to_be_activated.participant:
        if user_to_be_activated.is_active:
            messages.warning(request, 'User is already active')
            return redirect('account:account_list')
        else:
            user_to_be_activated.is_active = True
            user_to_be_activated.save()
            messages.success(request, 'User is successfully activated')
            return redirect('account:account_list')
    else:
        messages.error(request, 'Permission denied')
        return redirect('account:account_list')

@login_required
# @permission_required('account.can_activate_user', raise_exception=True)
def deactivate_user(request, user_id: int):
    if request.user.has_perm('account.can_activate_user') == False:
        messages.error(request, 'Unauthorized action')
        return redirect('account:account_list')
    user_to_be_activated = get_object_or_404(User, id=user_id)
    # check if the activating user is in the same organization as the activated user
    if request.user.is_superuser or request.user.participant == user_to_be_activated.participant:
        if not user_to_be_activated.is_active:
            messages.warning(request, 'User is already not active')
            return redirect('account:account_list')
        else:
            user_to_be_activated.is_active = False
            user_to_be_activated.save()
            messages.success(request, 'User is successfully deactivated')
            return redirect('account:account_list')
    else:
        messages.error(request, 'Permission denied')
        return redirect('account:account_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name: str = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {name}!')
            return redirect('home')
        else:
            messages.error('Something went wrong. Try again')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/users/register.html', {'form': form})
