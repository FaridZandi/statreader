# Generated by Django 3.0.1 on 2020-04-04 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_auto_20200102_2010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ('-name',)},
        ),
        migrations.CreateModel(
            name='StatHistoryDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='0', max_length=20, verbose_name='value')),
                ('date', models.DateField()),
                ('stat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Stat', verbose_name='stat')),
            ],
        ),
    ]
