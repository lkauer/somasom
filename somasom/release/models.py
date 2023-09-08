from django.db import models

# Create your models here.
class Release(models.Model):
    id_release = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nm_release = models.CharField(max_length=100)
    ds_release = models.CharField(max_length=500)
    ph_release = models.BinaryField(max_length=None)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)