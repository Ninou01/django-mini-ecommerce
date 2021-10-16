from django.contrib import admin

from .models import Produit, Commande


class ProduitAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['name', 'prix', 'prix_remise', 'en_stock']
    list_filter = ['prix', 'prix_remise', 'en_stock']


class CommandeAdmin(admin.ModelAdmin):
    # fields = ["produit", ("nom", "prenom"), "phone_number", "adress",
    #           "quantité", "etat", "date_commande", "date_reçu", ]
    exclude = ['annulé']
    list_display = ['__str__', 'etat', "phone_number1", "phone_number2", 'adress', 'quantité',
                    'date_commande', 'date_reçu', 'annulé']
    list_filter = ['etat', 'date_commande', 'date_reçu']
    list_editable = ['annulé']


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande, CommandeAdmin)
