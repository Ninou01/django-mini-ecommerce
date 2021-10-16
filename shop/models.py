from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
import datetime
from django.core.validators import RegexValidator

# Create your models here.


class Produit(models.Model):
    name = models.CharField(max_length=200)
    prix = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    prix_remise = models.FloatField(blank=True, null=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    en_stock = models.BooleanField(default=True)
    # image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Produit, self).save(*args, **kwargs)


COMMANDE_ETAT = (
    ("en attente", "en attente"),
    ("envoyer", "envoyer"),
    ("reçue", "reçue"),
)


class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)

    phone_regex = RegexValidator(
        regex=r'^0?\d{10,}$',
        message="votre numero de telephone doit commancer par un 0 et contenir 10 chifres"
    )
    phone_number1 = models.CharField(
        validators=[phone_regex], max_length=10)
    phone_number2 = models.CharField(
        validators=[phone_regex], max_length=10, blank=True, null=True)

    adress = models.CharField(max_length=500)
    quantité = models.PositiveIntegerField(default=1)
    etat = models.CharField(choices=COMMANDE_ETAT,
                            default="en attente", max_length=50)
    date_commande = models.DateTimeField(default=datetime.datetime.now())
    date_reçu = models.DateTimeField(blank=True, null=True)
    annulé = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} - {} {}".format(self.nom, self.prenom, self.quantité, self.produit)

    def get_total_amount(self):
        if self.produit.prix_remise:
            return self.produit.prix_remise * self.quantité
        else:
            return self.produit.prix * self.quantité

    def save(self, *args, **kwargs):
        if self.etat == "reçue":
            self.date_reçu = datetime.datetime.now()

        super(Commande, self).save(*args, **kwargs)


def delete_commande(sender, **kwargs):
    commandes = Commande.objects.all().filter(annulé=True)
    for commande in commandes:
        commande.delete()


post_save.connect(delete_commande, sender=Commande)
