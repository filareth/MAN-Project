# Generated by Django 4.2.7 on 2023-11-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crossword', '0002_rename_crossword_crosswords'),
    ]

    operations = [
        migrations.AddField(
            model_name='crosswords',
            name='posting_time',
            field=models.IntegerField(default=0),
        ),
    ]