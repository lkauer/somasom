from django.db import models
import uuid

# Create your models here.

class Artist(models.Model):
    id_artist = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_artist = models.CharField(max_length=100)
    ds_artist = models.CharField(max_length=500)
    ph_artist = models.CharField(max_length=500)

    def get_artist_by_id(self):
        return self