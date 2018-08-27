from django.forms import ModelForm
from gestionon_cheptel.models.models import Race, Animal, Categorie, Evenement, Cheptel, GroupeEmbouche, GroupeReproduction, Etat, Misebas, ProprietairePersonne, ProprietaireMoral, Animalevenmt
from django import forms

#++++++++++ Les formulaires des classes du modukle gestion cheptel +++++++++++

class CheptelForm(ModelForm):
    class Meta:
        model = Cheptel
        fields = '__all__'


###### FORMULAIRE POUR Animalevenmt ##########
class AnimalevenmtForm(ModelForm):
    class Meta:
        model = Animalevenmt
        fields = '__all__'
#         exclude = ['title']

###### FORMULAIRE POUR CHEPTEL EMBOUCHE ##########
class GroupeEmboucheForm(ModelForm):
    class Meta:
        model = GroupeEmbouche
        fields = '__all__'
#         exclude = ['title']

###### FORMULAIRE POUR RECHERCHER ###########
class RechercheForm(forms.Form):
    Recherche = forms.CharField(label='Rechercher', max_length=100)
    
        
#######FORMULAIRE POUR RACE ##################
class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = '__all__'
       
        
######## FORMULAIRE POUR POUR CATEGORIE ############
class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
        
        
######## FORMULAIRE POUR POUR EVENEMMENT ############
class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        fields = '__all__'
        
        
######## FORMULAIRE POUR POUR CHEPTEL REPRODUCTION ############
class GroupeReproductionForm(ModelForm):
    class Meta:
        model = GroupeReproduction
        fields = '__all__'
        

######## FORMULAIRE POUR POUR ETAT ############
class EtatForm(ModelForm):
    class Meta:
        model = Etat
        fields = '__all__'
        
######## FORMULAIRE POUR POUR MISE BAS ############
class MiseBasForm(ModelForm):
    class Meta:
        model = Misebas
        fields = '__all__'
        
        
######## FORMULAIRE POUR POUR PROPRIETAIRE ############
class ProprietairePersonneForm(ModelForm):
    class Meta:
        model = ProprietairePersonne
        fields = '__all__'

######## FORMULAIRE POUR POUR PROPRIETAIRE ############
class ProprietaireMoralForm(ModelForm):
    class Meta:
        model = ProprietaireMoral
        fields = '__all__'

###### FORMULAIRE POUR ANIMAL ##############
class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        