from django.db import models
from django.contrib.auth.models import User
from user.models import Profile
from uuid import uuid4

# class User(AbstractUser):
#     name = models.CharField(max_length=200,null=True)
#     email = models.EmailField(unique=True,null=True)
#     bio = models.TextField(null=True)

#     avatar = models.ImageField(upload_to='base', null=True, blank=True,default='base-default/avatar.svg')

#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = []
#     pass

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name[:50]
    pass


class Room(models.Model):
    host = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    participants = models.ManyToManyField(Profile,related_name="participants",blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name

    pass


class RoomMessage(models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.body[:25]
    pass
