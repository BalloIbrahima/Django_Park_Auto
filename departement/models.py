from django.db import models

# Create your models here.
class departement(models.Model):
    ID_Departement=models.AutoField(primary_key=True)
    Nom_Departement=models.CharField(max_length=255)
    Responsable_Departement=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.Nom_Departement}"