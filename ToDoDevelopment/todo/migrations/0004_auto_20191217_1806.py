# Generated by Django 2.1 on 2019-12-17 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todoitem_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='userID',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
