# Generated by Django 5.0.2 on 2024-04-19 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userdata_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='digitalEquivalent',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цифровой эквивалент уровня'),
        ),
    ]
