# Generated by Django 3.0.1 on 2020-01-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='stat',
            name='prefix',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='suffix',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]