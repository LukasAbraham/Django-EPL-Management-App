# Generated by Django 4.2 on 2023-06-11 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_fixture_remove_participatein_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='round_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fixture',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='login.team'),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='login.team'),
        ),
    ]
