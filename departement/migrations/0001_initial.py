# Generated by Django 5.0.1 on 2024-02-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departement',
            fields=[
                ('ID_Departement', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_Departement', models.CharField(max_length=255)),
                ('Responsable_Departement', models.CharField(max_length=255)),
            ],
        ),
    ]
