# Generated by Django 4.2 on 2023-06-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_alter_team_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(default='NotMeetRequirements', max_length=255),
        ),
    ]
