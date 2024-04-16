# Generated by Django 4.2.5 on 2024-03-15 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist', '0002_artist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='user',
        ),
        migrations.AddField(
            model_name='artist',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]