from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Adicione o campo de ID personalizado
    user_id = models.CharField(max_length=20, unique=True, primary_key=True)
