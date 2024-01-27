from django.db import models

# Create your models here.
class departement(models.Model):
    ID_Departement=models.AutoField(primary_key=True)
    Nom_Departement=models.CharField(max_length=255)
    Responsable_Departement=models.CharField(max_length=255)


class division(models.Model):
    ID_Division=models.AutoField(primary_key=True)
    division=models.ForeignKey(departement,on_delete=models.CASCADE)
    Nom_Division=models.CharField(max_length=255)
    Responsable_Division=models.CharField(max_length=255)
