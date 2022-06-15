# Generated by Django 4.0.4 on 2022-06-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0043_alter_event_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='postpone_period',
            field=models.CharField(choices=[('Days', 'Weeks')], default='Days', max_length=20),
        ),
    ]