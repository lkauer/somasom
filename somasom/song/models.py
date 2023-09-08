from django.db import models

# Create your models here.
class Song(models.Model):
    id_song = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_song = models.CharField(max_length=100)
    ds_song = models.CharField(max_length=500)
    sg_song = models.BinaryField(max_length=None)
    release = models.ForeignKey(Release, on_delete=models.CASCADE)