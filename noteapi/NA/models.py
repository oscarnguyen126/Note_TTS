from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
class User(AbstractUser):
    uuid = models.UUIDField(default=UUID4,max_length=64,editable=False,unique=True, primary_key=True,)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField( editable=True,blank=False, null=False,default=djnow,help_text=_('Thời điểm tạo'),)
    updated_at = models.DateTimeField(editable=True,blank=False,null=True,default=djnow,help_text=_('Thời điểm cập nhật'),)

    def __str__(self):
        return self.user_name

class Note(models.Model):
    uuid = models.UUIDField(default=UUID4,max_length=64,editable=False,unique=True, primary_key=True,)
    folder_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(editable=True, blank=False, null=False, default=djnow,help_text=_('Thời điểm tạo'), )
    updated_at = models.DateTimeField(editable=True, blank=False, null=True, default=djnow,help_text=_('Thời điểm cập nhật'), )

    def __str__(self):
        return self.content

class Folder(models.Model):
    uuid = models.UUIDField(default=UUID4,max_length=64,editable=False,unique=True, primary_key=True,)
    folder_name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=True, blank=False, null=False, default=djnow,help_text=_('Thời điểm tạo'), )
    updated_at = models.DateTimeField(editable=True, blank=False, null=True, default=djnow,help_text=_('Thời điểm cập nhật'), )

    def __str__(self):
        return self.folder_name
