# Generated by Django 2.1 on 2018-08-28 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mehtods',
            name='mhot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mehtods',
            name='mpersons',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='mehtods',
            name='myear',
            field=models.IntegerField(default=0),
        ),
    ]
