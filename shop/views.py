from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Commande
from .forms import CommandeForm

# Create your views here.


def shop_page(request):
    produits = Produit.objects.all()
    context = {
        "produits": produits
    }

    return render(request, 'shop.html', context)


def produit_page(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            #  (("nom", "prenom"), "phone_number1", "adress", "quantité",)
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            phone_number1 = form.cleaned_data.get('phone_number1')
            phone_number2 = form.cleaned_data.get('phone_number2')
            adress = form.cleaned_data.get('adress')
            quantité = form.cleaned_data.get('quantité')

            commande = Commande.objects.create(produit=produit,
                                               nom=nom,
                                               prenom=prenom,
                                               phone_number1=phone_number1,
                                               phone_number2=phone_number2,
                                               adress=adress,
                                               quantité=quantité)
            return redirect('/shop/%s' % slug)
    else:
        form = CommandeForm()

    context = {
        "produit": produit,
        "form": form
    }

    return render(request, 'produit.html', context)
