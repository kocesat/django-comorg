from django.shortcuts import render, get_object_or_404, redirect
from .models import Participant, User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import (
    UserRegistrationForm, 
    UserEditForm) 
from django.views.decorators.http import require_POST


def account_list(request):
    users = User.objects.select_related('participant').all()
    roles = Group.objects.values_list('name', flat=True)
    return render(request, 'account/users/list.html', {
        'users': users,
        'roles': roles,
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
            email: str = form.cleaned_data.get('email')
            name: str = form.cleaned_data.get('first_name')
            user = get_object_or_404(User, email=email)
            user.is_active=False
            user.save()
            messages.success(request, f'Account created for {name}!')
            return redirect('home')
        else:
            messages.error('Something went wrong. Try again')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/users/register.html', {'form': form})


@login_required
@require_POST
def role_assing(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    chosen_role = request.POST['chosen_role']
    group = Group.objects.get(name=chosen_role)

    if not request.user.has_perm('account.can_assing_role'):
        messages.error(request, 'Permission denied')
        return redirect('account:account_list')
    
    if not (request.user.groups.filter(name='SYSTEM_ADMIN') or request.user.participant == user.participant):
        messages.warning(request, 'You are not not SYSTEM_ADMIN or not in the same organization as User')
        return redirect('account:account_list')
    # if we got this far assing the role
    group.user_set.add(user)
    messages.success(request, 'Assigned the role successfully')
    return redirect('account:account_list')


@login_required
@require_POST
def role_deny(request, user_id: int, role: str):
    # TODO: Add group, permission check
    # TODO: Write deny assign logic
    pass
