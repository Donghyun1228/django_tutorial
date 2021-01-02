from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from .choice import *
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, email, name):
        user = self.model(
            user_id = user_id,
            email = email,
            name = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, name=None):
        user = self.create_user(user_id, password, email, name)
        user.is_superuser = True
        user.is_staff = True
        user.level = 0
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True, unique=True)
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=2)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"


