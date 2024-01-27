from django.db import models

# Create your models here.
class mission(models.Model):
    ID_Mission=models.AutoField(primary_key=True)
    Description=models.TextField()
    Date_Debut=models.DateField()
    Date_Fin=models.DateField()

    def __str__(self) -> str:
        return f"{self.Description}"
