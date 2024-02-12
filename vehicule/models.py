from django.db import models

# Create your models here.
class vehicule(models.Model):
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
    Modele = models.CharField(max_length=255)
    Immatriculation = models.CharField(max_length=255)
    Kilometrage = models.IntegerField()
    Date_Acquisition = models.DateField()
    Date_Mise_En_Service = models.DateField()
    Statut = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.ID_Vehicule} - {self.Marque} -{self.get_Statut_display()}"