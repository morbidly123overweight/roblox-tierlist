from django.db import models

class Hra_v_Robloxe(models.Model):
    meno_hry = models.CharField(max_length=255)
    obrazok = models.ImageField(upload_to='hry_obrazky/', null=True, blank=True)
    popis_hry = models.TextField(max_length=255)
    hlasy = models.CharField(max_length=255)