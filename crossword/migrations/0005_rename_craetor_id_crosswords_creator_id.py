# Generated by Django 4.2.7 on 2023-11-06 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crossword', '0004_rename_crator_id_crosswords_craetor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crosswords',
            old_name='craetor_id',
            new_name='creator_id',
        ),
    ]