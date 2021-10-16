from django.contrib import admin

from .models import Produit, Commande


class ProduitAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['name', 'prix', 'prix_remise', 'en_stock']
    list_filter = ['prix', 'prix_remise', 'en_stock']


class CommandeAdmin(admin.ModelAdmin):
    # fields = ["produit", ("nom", "prenom"), "phone_number", "adress",
    #           "quantité", "etat", "date_commande", "date_reçu", ]

    exclude = ['phone_number', 'annulé']
    list_display = ['__str__', 'etat', 'phone_number', 'adress', 'quantité',
                    'date_commande', 'date_reçu', 'annulé']
    list_editable = ['annulé']
    list_filter = ['etat', 'date_commande', 'date_reçu']


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande, CommandeAdmin)
