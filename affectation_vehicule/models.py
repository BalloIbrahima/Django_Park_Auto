from django.db import models

# Create your models here.
class affectationvehicule (models.Model):
    ID_Affectation = models.AutoField(primary_key=True)
    ID_Mission = models.CharField(max_length=100, unique=True)
    ID_Vehicule = models.CharField(max_length=100, unique=True)
    ID_Conducteur = models.CharField(max_length=100, unique=True)
    ID_Emplacement = models.CharField(max_length=100, unique=True)
    Date_Affectation = models.DateField()
    Date_Retour = models.DateField()
    def __str__(self):
        return f"{self.ID_Affectation} - {self.ID_Mission} - {self.ID_Vehicule}- {self.ID_Conducteur}- {self.ID_Emplacement}"