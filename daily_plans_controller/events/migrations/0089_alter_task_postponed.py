# Generated by Django 4.0.4 on 2022-06-15 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0088_alter_task_postponed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='postponed',
            field=models.DurationField(blank=True, choices=[(datetime.timedelta(days=1), 'One day'), (datetime.timedelta(days=3), 'Three days'), (datetime.timedelta(days=7), 'One week'), (datetime.timedelta(days=14), 'Two weeks'), (datetime.timedelta(days=28), 'One month')], default=datetime.timedelta(0), null=True),
        ),
    ]
