from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    nickname = models.CharField(verbose_name='昵称', max_length=32)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to = 'avatars/',default="/avatars/default.png")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.username
