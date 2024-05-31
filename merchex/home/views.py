from django.http import HttpResponse
from django.shortcuts import render
from home.models import FirstPage
from home.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from home.block import JourneyBanner


def home(request):
    firstpages = FirstPage.objects.first()
    journeys = JourneyBanner.objects.all()
    return render(request, 'home/first-page.html', {'firstpages' : firstpages, 'journeys' : journeys})

def cv(request):
    return render(request, 'home/cv.html')

def contact(request):
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject= f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
                    message=form.cleaned_data['message'],
                    from_email=form.cleaned_data['email'],
                    recipient_list=['admin@merchex.xyz'],
                    )
            return redirect('email-sent')
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()


    form = ContactUsForm() # ajout d’un nouveau formulaire ici
    return render(request,
    'home/contact.html',
    {'form': form}) # passe ce formulaire au gabarit

