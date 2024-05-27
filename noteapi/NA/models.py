from django.db import models
from django.utils.timezone import now as djnow

class User(models.Model):
    uuid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=djnow, editable=False)
    updated_at = models.DateTimeField(default=djnow, editable=False)

    def __str__(self):
        return self.user_name

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    folder_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(default=djnow(),editable=False)
    created_at = models.DateTimeField(default=djnow(),editable=False)

    def __str__(self):
        return self.content

class Folder(models.Model):
    folder_id = models.AutoField(primary_key = True)
    folder_name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=djnow(),editable=False)
    created_at = models.DateTimeField(default=djnow(),editable=False)

    def __str__(self):
        return self.folder_name
