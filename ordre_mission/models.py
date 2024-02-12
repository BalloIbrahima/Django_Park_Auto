from django.db import models

# Create your models here.
class ordremission (models.Model):
    ID_Ordre_Mission = models.AutoField(primary_key=True)
    ID_Departement = models.CharField(max_length=100, unique=True)
    Description = models.TextField()
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    def __str__(self):
        return f"{self.ID_Ordre_Mission} - {self.ID_Departement} - {self.Description}"