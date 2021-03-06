# Generated by Django 2.2.25 on 2022-01-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpd', '0004_auto_20220109_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bonus_package',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '1/2'), (4, 'K2'), (5, '3'), (6, 'K3')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='mng_end_user',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[(1, 'active'), (2, ' deactivated ')], max_length=200, null=True),
        ),
    ]
