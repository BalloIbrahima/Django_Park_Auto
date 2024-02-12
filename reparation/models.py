from django.db import models

# Create your models here.
class reparation(models.Model):
    ID_Reparation = models.AutoField(primary_key=True)
    ID_Vehicule = models.CharField(max_length=100, unique=True)
    Description_Panne = models.TextField()
    Date_Panne = models.DateField()
    Date_Reparation = models.DateField()
    Cout_Reparation = models.IntegerField()
    def __str__(self):
        return f"{self.ID_Reparation} - {self.ID_Vehicule} - {self.Description_Panne}"