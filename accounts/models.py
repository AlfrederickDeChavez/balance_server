from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, age, gender, height, weight, password=None): #

        if not email:
            raise ValueError('Users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, age=age, gender=gender, height=height, weight=weight)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, *args, **kwargs):

        user = self.create_user(email=email, username=username, age=0, gender='Male', height=171, weight=60, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    GENDER = [('Male', 'Male'), ('Female', 'Female')]
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=255, choices=GENDER, default='Male')
    height = models.FloatField()
    weight = models.FloatField()

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

