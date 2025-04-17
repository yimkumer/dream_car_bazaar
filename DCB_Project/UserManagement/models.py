from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from django.utils import timezone
from django.core.validators import RegexValidator
from DCB_Project.views import generate_unique_object_id
from django.db.models import Index
import datetime
import pytz
import os
from django.conf import settings

tz = pytz.timezone('Asia/Calcutta')
current_datetime = datetime.datetime.now(tz=tz)

GENDER = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Other', 'OTHER')
)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, password, **extra_fields):
        """
        Create and save a User with the given phone and password.
        """
        if not phone:
            raise ValueError('The Phone No. must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(default=generate_unique_object_id, primary_key=True, max_length=24)
    phone_regex = RegexValidator(regex=r'^[6789]\d{9}$',
                                 message="Phone number must be 10 digit no and started from 6 to 9 ...")
    phone = models.CharField(max_length=15, unique=True, validators=[phone_regex])
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    email = models.EmailField(max_length=80, unique=True)
    gender = models.CharField(max_length=30, choices=GENDER, null=True, blank=True)
    firm_name = models.CharField(max_length=90, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_signup = models.BooleanField(default=False)
    is_full_signup = models.BooleanField(default=False)
    user_image = models.ImageField(null=True, blank=True)
    user_image_url = models.URLField(null=True, blank=True)
    aadhar_card = models.ImageField(null=True, blank=True)
    pan_card = models.ImageField(null=True, blank=True)
    gst = models.ImageField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    def get_full_name(self):
        if self.first_name:
            if self.last_name:
                return str(self.first_name) + " " + str(self.last_name)
            else:
                return self.first_name
        else:
            return None

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'

