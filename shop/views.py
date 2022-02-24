from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produit, Commande
from .forms import CommandeForm


# Create your views here.


def shop_page(request):
    produits = Produit.objects.all().order_by('-id')
    context = {
        "produits": produits
    }

    return render(request, 'shop.html', context)


def produit_page(request, produit_id, slug):
    produit = get_object_or_404(Produit, id=produit_id, slug=slug)
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            pass
            full_name = form.cleaned_data.get('full_name')
            phone_number1 = form.cleaned_data.get('phone_number1')
            phone_number2 = form.cleaned_data.get('phone_number2')
            adresse = form.cleaned_data.get('adresse')
            quantité = form.cleaned_data.get('quantité')

            commande = Commande.objects.create(produit=produit,
                                               full_name=full_name,
                                               phone_number1=phone_number1,
                                               phone_number2=phone_number2,
                                               adresse=adresse,
                                               quantité=quantité)
            messages.add_message(request, messages.SUCCESS,
                                 'Votre commande a bien été prise')
            return redirect('/shop/{}/{}'.format(produit_id, slug))
    else:
        form = CommandeForm()

    context = {
        "produit": produit,
        "form": form,
        # "messages": messages
    }

    return render(request, 'produit-item.html', context)
