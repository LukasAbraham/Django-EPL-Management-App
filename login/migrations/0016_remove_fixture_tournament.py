# Generated by Django 4.2 on 2023-06-11 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_fixture_round_name_alter_fixture_team1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='tournament',
        ),
    ]
