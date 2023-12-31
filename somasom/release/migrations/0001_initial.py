# Generated by Django 4.2.5 on 2023-09-25 12:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0004_alter_artist_ph_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id_release', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nm_release', models.CharField(max_length=100)),
                ('ds_release', models.CharField(max_length=500)),
                ('ph_release', models.CharField(max_length=500)),
                ('fg_release', models.CharField(max_length=10)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
            ],
        ),
    ]
