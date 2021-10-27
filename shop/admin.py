from django.contrib import admin

from .models import Produit, Commande


class ProduitAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['name', 'prix', 'prix_remise', 'quantité_en_stock']
    list_filter = ['prix', 'prix_remise', ]


class CommandeAdmin(admin.ModelAdmin):

    list_display = ['id', 'full_name', 'quantité', 'produit', 'etat', 'phone__number', 'adresse',
                    'date_commande', 'date_confirmation', ]
    list_editable = ['etat', ]
    list_filter = ['etat', 'date_commande', 'date_confirmation']
    search_fields = ('full_name',)

    def phone__number(self, obj):
        if obj.phone_number2 != None:
            return "{}/{}".format(obj.phone_number1,
                                  obj.phone_number2)
        else:
            return obj.phone_number1

    phone__number.short_description = "Phone Number"


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande, CommandeAdmin)
