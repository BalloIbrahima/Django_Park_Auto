from django.db import models

# Create your models here.
class emplacement_parking(models.Model):
    OCCUPE = 'occupé'
    LIBRE = 'libre'
    DISPONIBILITE_CHOICES = [
        (OCCUPE, 'Occupé'),
        (LIBRE, 'Libre'),
    ]
    ID_Emplacement = models.AutoField(primary_key=True)
    Nom_Emplacement = models.CharField(max_length=255)
    Disponibilite = models.CharField(max_length=10,
    choices=DISPONIBILITE_CHOICES)
    def __str__(self):
        return f"{self.ID_Emplacement} - {self.Nom_Emplacement} -{self.get_disponibilite_display()}"