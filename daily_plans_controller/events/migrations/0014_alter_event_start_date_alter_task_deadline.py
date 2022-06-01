# Generated by Django 4.0.4 on 2022-05-31 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_event_start_date_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 13, 12, 59, 113935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 31, 13, 12, 59, 114225, tzinfo=utc)),
        ),
    ]
