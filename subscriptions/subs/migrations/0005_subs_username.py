# Generated by Django 4.0.6 on 2022-07-13 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subs', '0004_remove_subs_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='subs',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]