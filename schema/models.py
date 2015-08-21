from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)

    uuid = models.CharField('UID', max_length=100)

    def __str__(self):
        return self.user.get_username()

    def __unicode__(self):
        return self.user.get_username()
