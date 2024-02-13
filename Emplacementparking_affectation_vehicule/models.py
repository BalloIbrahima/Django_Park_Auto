from django.db import models

# Create your models here.
class emplacementparking(models.Model):
    OCCUPE = 'occupé'
    LIBRE = 'libre'

    DISPONIBILITE_CHOICES = [
        (OCCUPE, 'Occupé'),
        (LIBRE, 'Libre'),
    ]
    ID_Emplacement = models.AutoField(primary_key=True)
    Nom_Emplacement = models.CharField(max_length=255)
    Disponibilite = models.CharField(max_length=10,choices=DISPONIBILITE_CHOICES)
    def __str__(self):
        return f"{self.ID_Emplacement} - {self.Nom_Emplacement} - {self.get_disponibilite_display()}"
class mission(models.Model):
    ID_Mission = models.AutoField(primary_key=True)
    Description = models.TextField()
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    def __str__(self) -> str:
        return f"{self.Description}"

from django.db import models
class vehicule (models.Model):
    En_service = 'En service'
    En_reparation = 'En reparation'
    Hors_service = 'Hors service'

    Statut = [
        (En_service, 'En service'),
        (En_reparation, 'En reparation'),
        (Hors_service, 'Hors service'),
    ]
    ID_Vehicule = models.AutoField(primary_key=True)
    Marque = models.CharField(max_length=255)
    Modèle = models.CharField(max_length=255)
    Immatriculation = models.CharField(max_length=255)
    Kilometrage = models.IntegerField(max_length=255)
    Date_Acquisition = models.DateField()
    Date_Mise_En_Service = models.DateField()
    Statut = models.CharField(max_length=10, choices= Statut)
    def __str__(self):
        return f"{self.ID_Vehicule} - {self.Marque} - {self.get_Statut_display()}"
from django.db import models
class conducteur(models.Model):
    ID_Conducteur = models.AutoField(primary_key=True)
    Nom = models.TextField()
    Prenom = models.TextField()
    Numero_Telephone = models.TextField()

class affectationvehicule (models.Model):
    ID_Affectation = models.AutoField(primary_key=True)
    mission = models.ForeignKey(mission, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(conducteur, on_delete=models.CASCADE)
    emplacementparking = models.ForeignKey(emplacementparking,on_delete=models.CASCADE)
    Date_Affectation = models.DateField()
    Date_Retour = models.DateField()
    def __str__(self):
        return f"{self.ID_Affectation} - {self.ID_Mission} - {self.ID_Vehicule}- {self.ID_Conducteur}- {self.ID_Emplacement}"