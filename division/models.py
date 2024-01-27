from django.db import models

# Create your models here.
class division(models.Model):
    ID_Division=models.AutoField(primary_key=True)
    ID_Departement=models.CharField(max_length=255,unique=True)
    Nom_Division=models.CharField(max_length=255)
    Responsable_Division=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.ID_Division} - {self.ID_Departement} - {self.Nom_Division}"