# Generated by Django 4.1.7 on 2023-06-27 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0042_alter_player_stat_numberofassists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_stat',
            name='awaygoals',
            field=models.IntegerField(default=0),
        ),
    ]
