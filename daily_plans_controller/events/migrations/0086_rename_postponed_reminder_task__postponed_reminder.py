# Generated by Django 4.0.4 on 2022-06-15 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0085_alter_task_postponed_reminder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='postponed_reminder',
            new_name='_postponed_reminder',
        ),
    ]
