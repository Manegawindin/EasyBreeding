from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views import View
from gestionon_cheptel.forms.forms import AnimalForm, AnimalevenmtForm
from gestionon_cheptel.models.models import Race, Animal, Categorie, Evenement, Cheptel, GroupeEmbouche, GroupeReproduction, Etat, Misebas, ProprietairePersonne, ProprietaireMoral, Animalevenmt
from django.contrib.auth.decorators import login_required


# Create your views here.@login_required login_url="{% url 'login' %}"



class IndexView(generic.ListView):
    model = GroupeReproduction
    template_name = 'gestionon_cheptel/accueil.html'

@login_required
def index2(request):
    return render (request, 'cheptel/index.html')
#     return HttpResponse (templates/home/index.html)
#     template = loader.get_template('home/index.html')
#     return HttpResponse(template.render(request))

@login_required
def creerCheptel(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
#             return HttpResponseRedirect('/thanks/')
    else:
        form=AnimalForm()
    return render (request, 'gestionon_cheptel/creerCheptel.html', {'form':form})


@login_required
def CreerEvenement(request):
    if request.method == 'POST':
        form = AnimalevenmtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
#             return HttpResponseRedirect('/thanks/')
    else:
        form=AnimalevenmtForm()
    return render (request, 'gestionon_cheptel/creerEvenement.html', {'form':form})


        
