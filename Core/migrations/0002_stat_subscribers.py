# Generated by Django 3.0.1 on 2020-01-02 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribed_stats', to=settings.AUTH_USER_MODEL),
        ),
    ]
