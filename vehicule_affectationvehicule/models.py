from django.db import models

# Create your models here.
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
        return f'{self.ID_Vehicule} - {self.Marque} - {self.get_Statut_display()}'

class affectationvehicule (models.Model):
    ID_Affectation = models.AutoField(primary_key=True)
    vehicule = models.ForeignKey(vehicule, on_delete=models.CASCADE)
    Date_Affectation = models.DateField()
    Date_Retour = models.DateField()
    def __str__(self):
        return f'{self.ID_Affectation}- {self.ID_Vehicule}'