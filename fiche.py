# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Groupeutilisateur(models.Model):
    libelle = models.CharField(max_length=254, 'Libelle')
    typeGroupe = models.CharField('type du Groupe', max_length=254, 'Type du groupe')  
    

class Affecte(models.Model):
    groupe = models.ForeignKey(Groupeutilisateur, on_delete=models.CASCADE, 'Groupe')
    dateAffectation = models.DateTimeField('date d\'affectation')

class Categorie(models.Model):
    description = models.TextField('Description')


class Race(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, 'Categorie')
    nomRace = models.CharField(max_length=254, 'Nom')
    zoneProvenance = models.CharField(max_length=254, 'Zone de provenance')


class Animal(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, 'Race')
    sexeAnimal = models.CharField(max_length=254, 'Sexe')
    anneeNaissance = models.DateTimeField('Date de Naissance')
    couleur = models.CharField(max_length=254, 'Couleur')
    dateAchat = models.DateTimeField('Date d\'achat')
    prixAchat = models.FloatField('Prix d\'achat')
    temperament = models.CharField(max_length=254, 'Temperament')
    conformation = models.CharField(max_length=254, 'Conformation')



class Evenement(models.Model):
    evenement = models.CharField(max_length=254, 'Evenement')



class Animalevenmt(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, 'Evenement')  
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, 'Animal') 
    dateEvenement = models.DateTimeField('Date de l\'evenement')  
    observation = models.TextField('Observation')




class Proprietaire(models.Model):
    groupe = models.ForeignKey(Groupeutilisateur, on_delete=models.CASCADE, 'Groupe du proriétaire')
    adresse = models.TextField('Adresse')
    email = models.EmailField('Email')
    tel = models.IntegerField('Numero de Telephone')
    motPasse = models.CharField(max_length=254, 'Mot de passe')



class Cheptel(models.Model):
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, 'Propriétaire')
    nombreAnimaux = models.IntegerField('Nombre d\'animaux')
    nomCheptel = models.CharField(max_length=254, 'Nom Cheptel')



class Cheptelembouche(models.Model):
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE, 'Cheptel')
    nombreAnimaux = models.IntegerField('Nombre d\'animaux')
    typeEmbouche = models.CharField(max_length=254, 'Type d\'embouche')
    duree = models.IntegerField('Durée en mois')



class Cheptelreproduction(models.Model):
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE, 'Cheptel')
    nombreMale = models.IntegerField('Nombre de male')
    nombreFemelle = models.IntegerField('Nombre de femelle')



class Etat(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, 'Animal')
    taille = models.IntegerField('Taille en cm')
    sante = models.CharField(max_length=254, 'Sante')
    menstruation = models.CharField(max_length=254,'Menstruation')
    datePrise = models.DateTimeField('Date de prise')



class Groupeanimaux(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, 'Animal')
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE, 'Cheptel')
    libelle = models.CharField(max_length=254, 'Libellé')



class Groupepersonne(models.Model):
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, 'Propriétaire')
    nomGroupe = models.CharField(max_length=254, 'Nom du groupe')
    nombrePersonne = models.CharField(max_length=254, 'Nombre de Personne')



class Misebas(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, 'Animal')
    dateMisebas = models.DateTimeField('Date de mise bas')
    nombre = models.IntegerField('Nombre')
    description = models.TextField('Description')



class Personne(models.Model):
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, 'Propriétaire')
    nom = models.CharField(max_length=254, 'Nom')
    prenom = models.CharField(max_length=254, 'Prénom')
    sexe = models.CharField(max_length=254, 'Sexe')
    dateNaissance = models.DateField('Date de naissance')
