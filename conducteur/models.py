from django.db import models

# Create your models here.
class conducteur(models.Model):
    ID_Conducteur=models.AutoField(primary_key=True)
    Nom=models.TextField()
    Prenom=models.DateField()
    Numero_Telephone=models.DateField()

    def __str__(self) -> str:
        return f"{self.Numero_Telephone}"
    