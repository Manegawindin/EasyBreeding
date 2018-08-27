from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Le times tamps
class TimespamtedModel(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True
#--------------------------------------------


#class categorie de betail :Bovin ou Ovin
class Categorie(TimespamtedModel):
	"les animaux seront classés selon des categories"
	nomCategorie = models.CharField(blank=True,max_length=50, null=True, verbose_name='Nom de la categorie')
	libelleCategorie = models.CharField(blank=True,max_length=100, null=True, verbose_name='libelle de la categorie')
	descriptionCategorie = models.CharField(blank=True,max_length=255, null=True, verbose_name='Description de la categorie')


	def init(self,nom,libelle,description):
		self.nomCategorie=nom
		self.libelleCategorie=libelle
		self.descriptionCategorie=description

	def __str__(self):
		return u'%s %s' %(self.nomCategorie,self.libelleCategorie)
#-----------------------FIN class categorie--------------------------------

#classe evenement (un evenement est observe sur un animal:il peut s'agit d'une infection,mise-bas,etc)

class Evenement(TimespamtedModel):
	"Un poura etre observé sur un animal ou plusieurs animaux données"
	libelleEvenement = models.CharField(max_length=100, verbose_name='Libelle evenement', blank=True)
	evenement = models.CharField(max_length=254, verbose_name='Type evenement ', blank=True, null=True)
	observation = models.CharField(max_length=254, verbose_name='Observation', blank=True, null=True)

	"Les methodes implementées par le model"
	def init(self,libelle,evenement,observation):
		self.libelleEvenement=libelle
		self.evenement=evenement
		self.observation=observation

	def __str__(self):
		return u'%s %s'%(self.libelleEvenement, self.evenement)
#--------------------------FIN class evenement animal------------------------------

#classe Race des animaux : chaque animal appartient a une race et la race est logéé dans une categorie donnée
class Race(TimespamtedModel):
	"Classe pour specification des attibuts de la classe race"
	categorie = models.ForeignKey(Categorie, db_column='idCategorie', on_delete=models.PROTECT)  # Field name made lowercase.
	nomRace = models.CharField(db_column='nomRace', max_length=100, verbose_name='Nom de la Race', blank=True)  # Field name made lowercase.
	zoneProvenance = models.CharField(db_column='zoneProvenance', verbose_name='Zone de Provenance', max_length=100, blank=True, null=True)
	tailleMax = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Taille maximale')
	poidsMax = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Poids maximal')
	conformation = models.CharField(max_length=50)
	carcasse = models.CharField(max_length=50)

    

	"Les methodes de la classe race"
	def init(self,nomrace,zone):
		self.nomRace=nomrace
		self.zoneProvenance=zone

	def __str__(self):
		return u'%s %s'%(self.nomRace,self.zoneProvenance)
#------------------------FIN classe class----------------------------------
		



#Classe Proprietaire
class Proprietaire(TimespamtedModel):
	adresse = models.CharField(max_length=100)
	telephone = models.CharField(max_length=100)
	Ville = models.CharField(max_length=100)
	Pays = models.CharField(max_length=100)

	class Meta:
		abstract = False	
#----------------FIN de la classe Proprietaire----------------------------------------------



#Classe ProprietairePersonne
class ProprietairePersonne(Proprietaire):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=254)
	choix=(
        ('M', 'Male'),
        ('F', 'Femelle'),
        )
	sexe = models.CharField('sexe', max_length=1, choices=choix)
	dateNaissace = models.DateField()
	lieuNaissance = models.CharField(max_length=100)	
#----------------FIN de la classe ProprietairePersonne----------------------------------------------	


#Classe ProprietaireMoral
class ProprietaireMoral(Proprietaire):
	nom = models.CharField(max_length=100)
	representant1 = models.ForeignKey(User, on_delete=models.PROTECT)
	representant2 = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='+')
	representan3 = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='+')
#----------------FIN de la classe ProprietairePersonne----------------------------------------------


#Classe Cheptel
class Cheptel(TimespamtedModel):
	proprietaire = models.ForeignKey(Proprietaire, on_delete=models.PROTECT)
	nom = models.CharField(max_length=100)
	ville = models.CharField(max_length=100)
	secteur = models.CharField(max_length=100)
	superficie = models.FloatField(verbose_name='superficie de la ferme')
    
    	
	def __str__(self):
		return self.nom
#---------------------FIN classe Mis-bas-------------------------------------------------


#classe Groupe des animaux : chaque animal appartient a un groupe et le groupe est logéé dans un cheptel
class GroupeAnimal(TimespamtedModel):
	"Classe pour specification des attibuts de la classe GroupeAnimal"
	cheptel = models.ForeignKey(Cheptel, on_delete=models.PROTECT)
	libelle = models.CharField(max_length=100)
	dateArrive = models.DateField()

	class Meta:
		abstract = False     

	"Les methodes de la classe race"
	def init(self,cheptel,libelle,dateArrive):
		self.cheptel=cheptel
		self.libelle=libelle
		self.dateArrive=dateArrive


	def __str__(self):
		return u'%s %s %s'%(self.cheptel,self.libelle,self.dateArrive)
#------------------------FIN classe class----------------------------------



#Classe Cheptel Embouche
class GroupeEmbouche(GroupeAnimal):
	duree = models.IntegerField('durée en mois')
	typeEmbouche = models.CharField('Type de l\'embouche', max_length=100)
	def __str__(self):
		return self.GroupeAnimal
#---------------------FIN classe Cheptel Embouche-----------------------------------------

#Classe cheptel Remproduction
class GroupeReproduction(GroupeAnimal):

	def __str__(self):
		return self.GroupeAnimal
#---------------------FIN classe Mis-bas--------------------------------------------------


#Classe animal :Identification d'un animal
class Animal(TimespamtedModel):
	groupe = models.ForeignKey(GroupeAnimal, on_delete=models.PROTECT)
	choix=(
        ('M', 'Male'),
        ('F', 'Femelle'),
        )
	nom = models.CharField(max_length=254)
	race = models.ForeignKey(Race, on_delete=models.PROTECT)
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


#class AnimalAcheter(Animal):
#   "Classe heritant la classe Animal"
#    dateachat = models.DateTimeField(db_column='dateAchat', verbose_name='Date achat animal', blank=True, null=True)  # Field name made lowercase.
#    prixachat = models.FloatField(db_column='prixAchat',verbose_name='Prix achat', blank=True, null=True)  # Field name made lowercase.

#    class Meta:
#        managed = False
#       db_table = 'Animal'


#class AnimalReproduit(Animal):
#    "classe herité de la classe abstraite Animal"
#    annenaissance = models.DateTimeField(db_column='anneNaissance',verbose_name='Date de naissance', blank=True, null=True)  # Field name made lowercase.

 #   class Meta:
  #      managed = False
  #      db_table = 'Animal'

#---------------------------Fin des classe---------------------------------------------

#classe d'association animal evenement

class Animalevenmt(TimespamtedModel):
    evenement = models.ForeignKey(Evenement, on_delete=models.PROTECT)  
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT) 
    dateEvenement = models.DateTimeField('date de l\'evenement')  
    observation = models.TextField('observation')
    
    def __str__(self):
        return self.evenement
#-------------------FIN classe AnimalEvent--------------------------------------------

#Classe Mise bas: 
class Misebas(TimespamtedModel):
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    dateMisebas = models.DateTimeField('date de mise bas')
    nombre = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.nombre
#---------------------FIN classe Mis-bas-------------------------------------------------


#Classe Etat animal
class Etat(TimespamtedModel):
	animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
	taille = models.FloatField('taille en cm')
	poids = models.FloatField(verbose_name='Poids en kg')
	sante = models.CharField(max_length=254)
	datePrise = models.DateTimeField('date de prise')
	photo = models.ImageField()
    
	def __str__(self):
		return self.sante
#----------------------------------------Fin classe Etat-----------------------------------