from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Groupeutilisateur(models.Model):
    libelle = models.CharField( max_length=254)
    typeGroupe = models.CharField('type du Groupe', max_length=254)
    
    def __str__(self):
        return self.libelle  
    

class Affecte(models.Model):
    groupe = models.ForeignKey(Groupeutilisateur, on_delete=models.CASCADE)
    dateAffectation = models.DateTimeField('date d\'affectation')

class Categorie(models.Model):
    nomCategorie = models.CharField(max_length=254)
    libelleCategorie = models.CharField(max_length=254)
    description = models.TextField()
    
    def __str__(self):
        return self.description


class Race(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nomRace = models.CharField('nom', max_length=254)
    zoneProvenance = models.CharField('zone de provenance', max_length=254)
    
    def __str__(self):
        return self.nomRace



class Evenement(models.Model):
    evenement = models.CharField(max_length=254)
    
    def __str__(self):
        return self.evenement
    
    

class Animal(models.Model):
    choix=(
        ('M', 'Male'),
        ('F', 'Femelle'),
        )
    nom = models.CharField(max_length=254)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    sexeAnimal = models.CharField('sexe', max_length=1, choices=choix)
    anneeNaissance = models.DateField('date de Naissance')
    couleur = models.CharField(max_length=254)
    dateAchat = models.DateField('date d\'achat')
    prixAchat = models.FloatField('prix d\'achat')
    temperament = models.CharField(max_length=254)
    conformation = models.CharField(max_length=254)
    evenements = models.ManyToManyField(Evenement, through='Animalevenmt', through_fields=('animal', 'evenement'),)
    
    def __str__(self):
        return self.nom




class Animalevenmt(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)  
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE) 
    dateEvenement = models.DateTimeField('date de l\'evenement')  
    observation = models.TextField('observation')
    
    def __str__(self):
        return self.evenement




class Proprietaire(models.Model):
    groupe = models.ForeignKey(Groupeutilisateur, on_delete=models.CASCADE)
    adresse = models.TextField()
    email = models.EmailField()
    tel = models.IntegerField('numero de Telephone')
    motPasse = models.CharField('mot de passe', max_length=254)
    
    def __str__(self):
        return self.groupe.libelle



class Cheptel(models.Model):
    Proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    nombreAnimaux = models.IntegerField('nombre d\'animaux')
    nomCheptel = models.CharField('nom du Cheptel', max_length=254)
    
    def __str__(self):
        return self.nomCheptel



class Cheptelembouche(models.Model):
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE)
    nombreAnimaux = models.IntegerField('nombre d\'animaux')
    typeEmbouche = models.CharField('type d\'embouche', max_length=254)
    duree = models.IntegerField('durée en mois')
    
    def __str__(self):
        return self.cheptel



class Cheptelreproduction(models.Model):
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE)
    nombreMale = models.IntegerField('nombre de male')
    nombreFemelle = models.IntegerField('nombre de femelle')
    
    def __str__(self):
        return self.cheptel



class Etat(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    taille = models.IntegerField('taille en cm')
    sante = models.CharField(max_length=254)
    menstruation = models.CharField(max_length=254)
    datePrise = models.DateTimeField('date de prise')
    
    def __str__(self):
        return self.sante



class Groupeanimaux(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    cheptel = models.ForeignKey(Cheptel, on_delete=models.CASCADE)
    libelle = models.CharField('libellé', max_length=254)
    
    def __str__(self):
        return self.libelle



class Groupepersonne(models.Model):
    Proprietaire = models.ForeignKey(Proprietaire,verbose_name='propriétaire', on_delete=models.CASCADE)
    nomGroupe = models.CharField('nom du groupe', max_length=254)
    nombrePersonne = models.IntegerField('nombre de Personne')
    
    def __str__(self):
        return self.nomGroupe



class Misebas(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    dateMisebas = models.DateTimeField('date de mise bas')
    nombre = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.nombre



class Personne(models.Model):
    choix=(
        ('M', 'Masculin'),
        ('F', 'Feminin'),
        )
    Proprietaire = models.ForeignKey(Proprietaire, verbose_name='propriétaire', on_delete=models.CASCADE)
    nom = models.CharField('nom', max_length=254)
    prenom = models.CharField('prénom', max_length=254)
    sexe = models.CharField(max_length=1, choices=choix)
    dateNaissance = models.DateField('date de naissance')
    
    def __str__(self):
        return self.prenom
