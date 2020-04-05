# Generated by Django 3.0.1 on 2020-04-05 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0006_auto_20200404_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stathistorydaily',
            options={'verbose_name': 'Stat History (Daily)', 'verbose_name_plural': 'Stat History (Daily)'},
        ),
        migrations.AlterField(
            model_name='stat',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='subscribed_stats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stathistorydaily',
            name='stat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stat_histories_daily', to='Core.Stat', verbose_name='stat'),
        ),
        migrations.CreateModel(
            name='StatHistoryHourly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='0', max_length=20, verbose_name='value')),
                ('hour', models.DateTimeField()),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stat_histories_hourly', to='Core.Stat', verbose_name='stat')),
            ],
            options={
                'verbose_name': 'Stat History (Hourly)',
                'verbose_name_plural': 'Stat History (Hourly)',
            },
        ),
    ]