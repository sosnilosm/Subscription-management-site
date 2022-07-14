from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Subs(models.Model):
    name = models.CharField('Subscription name', max_length=50)
    cost = models.IntegerField('Subscription cost')
    distributor = models.CharField('Subscription distributor', max_length=50)
    start_date = models.DateField('Subscription date')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,
                             null=True)

    def __str__(self):
        return f'Subscription: {self.name}'

    class Meta:
        verbose_name = 'Sub'
        verbose_name_plural = 'Subs'
