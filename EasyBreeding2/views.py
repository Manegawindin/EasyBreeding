from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# ajout de email dans les champs
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage

from .forms import SignUpForm


def index(request):
    return render(request, 'index.html')


# def UserCreationView(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('accueil')
#     else:
#         form = SignUpForm()
#     return render(request, 'user/user_creation.html', {'form': form})


def UserCreationView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation de compte'
            message = render_to_string('user/user_creation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
                # urlsafe_base64_decode() decodes to bytestring
                #'uid' = urlsafe_base64_decode(uidb64).decode(),
                #'user' = UserModel._default_manager.get(pk=uid),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Confirmez votre email pour continuer l\'inscription s\'il vous plait.')
    else:
        form = SignUpForm()
    return render(request, 'user/user_creation.html', {'form': form})

# def UserCreationView(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'user/user_create_success.html')
#     else:
#         form = UserCreationForm()
#     context={"form":form,}
#     return render (request, 'user/user_creation.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render (request,'user/create_success.html')
    else:
        return HttpResponse('Lien d\'activation invalide!')