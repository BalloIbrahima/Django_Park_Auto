from django.db import models

# Create your models here.
class vehicule(models.Model):

    En_Service='En Service'
    En_Reparation='En Reparation'
    Hors_Service='En Service'

    Statut=[
        (En_Service,'En service')
        (En_Reparation='En Reparation')
        (Hors_Service='En Service')
    ]

    ID_Vehicule=models.AutoField(primary_key=True)
    Marque=models.CharField(max_length=255)
    Modele=models.CharField(max_length=255)
    Immatriculation=models.CharField(max_length=255)
    Kilometrage=models.IntegerField(max_length=255)
    Date_Acquisition=models.DateField()
    Date_Mise_En_Service=models.DateField()

    Statut=models.CharField(max_length=10,choices=Statut)
    # ID_Vehicule=models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return f"{self.ID_Vehicule} - {self.Marque} - {self.Statut} - {self.Immatriculation} - {self.get_Statut_display()}"