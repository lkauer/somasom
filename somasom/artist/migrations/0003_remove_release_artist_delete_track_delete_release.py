# Generated by Django 4.2.5 on 2023-09-20 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_release_song_track'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.DeleteModel(
            name='Release',
        ),
    ]
