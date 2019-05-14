from django.db import models
from django.conf import settings
from users.models import Profile

class Hangout(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, \
    on_delete = models.CASCADE)
  title = models.CharField(max_length=30, blank=True, null=True)
  members = models.ManyToManyField(Profile)
  description = models.TextField(blank=True, null=True)
  location = models.CharField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  date_of_event = models.DateTimeField()

  def __str__(self):
    return self.title

class Comment(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, \
    on_delete = models.CASCADE)
  hangout = models.ForeignKey(Hangout, \
    on_delete = models.CASCADE)
  content = models.TextField(blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.author.username



