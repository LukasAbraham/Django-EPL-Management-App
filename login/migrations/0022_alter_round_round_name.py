# Generated by Django 4.2 on 2023-06-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_round_alter_fixture_round_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='round_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
