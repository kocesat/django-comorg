from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .validators import participant_code_not_zero


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password

        Returns:
            [User]: Custom User Model
        """
        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Create and save a superuser with the given email and password
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(email, password, **extra_fields)


class Participant(models.Model):
    name = models.CharField(max_length=140)
    code = models.CharField(max_length=4, unique=True, validators=[participant_code_not_zero])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'participants'
        ordering = ('code', )

    def __str__(self):
        return f'{self.code} {self.name}'


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    participant = models.ForeignKey(
        Participant, 
        on_delete=models.CASCADE,
        related_name='users')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['participant']

    objects = UserManager()

    def __str__(self):
        return self.email
