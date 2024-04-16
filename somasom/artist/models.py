from django.db import models
import uuid
from manager.models import CustomUser

class Artist(models.Model):
    id_artist = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_artist = models.CharField(max_length=100)
    ds_artist = models.CharField(max_length=500)
    ph_artist = models.ImageField(upload_to='ph_artist/')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def get_artist_by_id(self):
        return self