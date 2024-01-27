from django.db import models

# Create your models here.
class agent(models.Model):
    ID_Agent=models.AutoField(primary_key=True)
    Nom=models.CharField(max_length=255)
    Prenom=models.CharField(max_length=255)
    Numero_Telephone=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.Numero_Telephone}"
    

