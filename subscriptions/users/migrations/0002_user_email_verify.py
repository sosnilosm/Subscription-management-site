# Generated by Django 4.0.6 on 2022-07-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
