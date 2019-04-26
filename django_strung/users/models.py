from django.db import models
from django.conf import settings

class Instrument(models.Model):
  name = models.CharField(max_length=50)


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, \
    on_delete=models.CASCADE)
  date_of_birth = models.DateField(blank=True, null=True)
  photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
  instruments = models.ManyToManyField(Instrument, blank=True)
  bio = models.TextField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return 'Profile for user {}'.format(self.user.username)

