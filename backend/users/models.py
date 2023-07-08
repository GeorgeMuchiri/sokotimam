
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class NewUserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password, phone, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, firstname=firstname, lastname=lastname, phone=phone, **other_fields)
        user.set_password(password)
        other_fields.setdefault('is_active', True)
        user.save()
        return user

    def create_superuser(self, email, username, firstname, lastname, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        if other_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned to is_active=True') 

        return self.create_user(email, username, firstname, lastname, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email  = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    startdate = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    objects = NewUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'phone']


    def __str__(self):
        return self.username
