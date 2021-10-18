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
    list_display = ['full_nmae', 'quantité', 'produit', 'etat', 'phone__number', 'adress',
                    'date_commande', 'date_reçu', 'annulé']
    list_editable = ['etat', 'annulé']
    list_filter = ['etat', 'date_commande', 'date_reçu']
    search_fields = ("nom", "prenom")

    def full_nmae(self, obj):
        return "{} {}" .format(obj.nom, obj.prenom)

    def phone__number(self, obj):
        if obj.phone_number2 != None:
            return "{}/{}".format(obj.phone_number1,
                                  obj.phone_number2)
        else:
            return obj.phone_number1

    full_nmae.short_description = "Full Name"
    phone__number.short_description = "Phone Number"


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande, CommandeAdmin)
