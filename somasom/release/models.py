from django.db import models
from artist.models import Artist
import uuid

# Create your models here.
class Release(models.Model):
    id_release = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_release = models.CharField(max_length=100)
    ds_release = models.CharField(max_length=500)
    ph_release = models.CharField(max_length=500)
    fg_release = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='releases')
