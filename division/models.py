from django.db import models

# Create your models here.
class division(models.Model):
    ID_Division=models.AutoField(primary_key=True)
    Nom_Division=models.TextField()
    Responsable_Division=models.TextField()

    def __str__(self) -> str:
        return f"{self.Nom_Division}"