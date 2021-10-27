from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):

    class Meta:
        model = Commande
        fields = ("full_name", "adresse", "phone_number1",
                  "phone_number2", "quantité",)

    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = "Nom et Prenom"
        self.fields['adresse'].widget.attrs['placeholder'] = "Adresse"
        self.fields['phone_number1'].widget.attrs['placeholder'] = "Numero De Telephone"
        self.fields['phone_number2'].widget.attrs[
            'placeholder'] = "Second Numero De Telephone (optionel)"
