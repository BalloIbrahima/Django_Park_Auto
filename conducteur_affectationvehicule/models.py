from django.db import models

# Create your models here.
class conducteur(models.Model):
    ID_Conducteur = models.AutoField(primary_key=True)
    Nom = models.TextField()
    Prenom = models.TextField()
    Numero_Telephone = models.TextField()

class affectationvehicule(models.Model):
    ID_Affectation = models.AutoField(primary_key=True)
    conducteur = models.ForeignKey(conducteur, on_delete=models.CASCADE)
    ID_Mission = models.CharField(max_length=100, unique=True)
    ID_Vehicule = models.CharField(max_length=100, unique=True)
    ID_Conducteur = models.CharField(max_length=100, unique=True)
    ID_Emplacement = models.CharField(max_length=100, unique=True)
    Date_Affectation = models.DateField()
    Date_Retour = models.DateField()