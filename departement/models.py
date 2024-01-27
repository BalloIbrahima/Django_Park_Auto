from django.db import models

# Create your models here.
class departement(models.Model):
    ID_Departement=models.AutoField(primary_key=True)
    Nom_Departement=models.TextField()
    Responsable_Departement=models.TextField()

    def __str__(self) -> str:
        return f"{self.Nom_Departement}"