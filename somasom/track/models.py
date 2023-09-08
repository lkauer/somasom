from django.db import models
from song.models import Song
import uuid

# Create your models here.
class Track(models.Model):
    id_track = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_track = models.CharField(max_length=100)
    ds_track = models.CharField(max_length=500)
    sg_track = models.BinaryField(max_length=None)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)