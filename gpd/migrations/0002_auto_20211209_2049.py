# Generated by Django 2.2.25 on 2021-12-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='NTUser_ID',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='person',
            name='surname',
            field=models.CharField(default='', max_length=30),
        ),
    ]