from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Participant
from .forms import UserRegistrationForm, UserEditForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserEditForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'participant')
    list_filter = ('email', 'is_staff', 'is_active', 'participant')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'participant', 'is_staff', 'is_active',)
        }),
    )
    search_fields = ('email', 'participant')
    ordering = ('email', )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Participant)