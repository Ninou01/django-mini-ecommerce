from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
import os
import datetime
from ckeditor.fields import RichTextField

# Create your models here.

def slugify_unicode(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

class Produit(models.Model):
    name = models.CharField(max_length=200)
    prix = models.PositiveIntegerField()
    prix_remise = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField(blank=True)
    # description = models.TextField(blank=True, null=True)
    description = RichTextField()
    quantité_en_stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='shop/produits/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify_unicode(self.name)
        super(Produit, self).save(*args, **kwargs)


COMMANDE_ETAT = (
    ("en attente", "en attente"),
    ("confirmé", "confirmé"),
    ("non confitmé", "non confitmé"),
)


class Commande(models.Model):
    produit = models.ForeignKey(
        Produit, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=200)

    phone_regex = RegexValidator(
        regex=r'^0?\d{10,}$',
        message="votre numero de telephone doit commancer par un 0 et contenir 10 chifres"
    )
    phone_number1 = models.CharField(
        validators=[phone_regex], max_length=10)
    phone_number2 = models.CharField(
        validators=[phone_regex], max_length=10, blank=True, null=True)

    adresse = models.CharField(max_length=500)
    quantité = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), ])
    etat = models.CharField(choices=COMMANDE_ETAT,
                            default="en attente", max_length=50)
    date_commande = models.DateTimeField(default=datetime.datetime.now())
    date_confirmation = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.etat == "confirmé":
            self.date_confirmation = datetime.datetime.now()
        super(Commande, self).save(*args, **kwargs)


