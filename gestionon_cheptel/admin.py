from django.contrib import admin

# Register your models here.
from gestionon_cheptel.models.models import Race, Animal, Categorie, Evenement, Cheptel, GroupeEmbouche, GroupeReproduction, Etat, Misebas, ProprietairePersonne, ProprietaireMoral, Animalevenmt
  
admin.site.register(Race)
admin.site.register(Animal)
admin.site.register(Categorie)
admin.site.register(Evenement)
admin.site.register(Cheptel)
admin.site.register(GroupeEmbouche)
admin.site.register(GroupeReproduction)
admin.site.register(Etat)
admin.site.register(Misebas)
admin.site.register(ProprietairePersonne)
admin.site.register(ProprietaireMoral)
admin.site.register(Animalevenmt)


