# Generated by Django 4.2 on 2023-06-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='goal_events',
            field=models.ManyToManyField(related_name='goal_events', through='login.GoalEvent', to='login.player'),
        ),
    ]
