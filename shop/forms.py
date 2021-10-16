from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):

    class Meta:
        model = Commande
        fields = ("nom", "prenom", "phone_number1",
                  "phone_number2", "adress", "quantité",)
