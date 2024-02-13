from django.db import models

# Create your models here.
class mission(models.Model):
    ID_Mission = models.AutoField(primary_key=True)
    Description = models.TextField()
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    def __str__(self) -> str:
        return f"{self.Description}"

class affectationvehicule (models.Model):
    ID_Affectation = models.AutoField(primary_key=True)
    mission = models.ForeignKey(mission, on_delete=models.CASCADE)
    Date_Affectation = models.DateField()
    Date_Retour = models.DateField()
    def __str__(self):
        return f"{self.ID_Affectation} - {self.ID_Mission}"