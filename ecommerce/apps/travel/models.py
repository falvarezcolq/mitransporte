""" Travel models """

# Django
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ecommerce.apps.account.models import Customer
from ecommerce.utils.models import ImageModel

class Company(models.Model):
    """
    Company of user
    """
    user = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="company")

    name = models.CharField(verbose_name="Nombre de la empresa",
                            help_text=_("Required and unique"),
                            max_length=255,
                            unique=True,
                            )
    razon_social = models.CharField(verbose_name="Nombre de la empresa",
                            help_text=_("Required and unique"),
                            max_length=255,
                            )
    nit = models.CharField(verbose_name="NIT",
                            help_text=_("Required and unique"),
                            max_length=255,
                            unique=True,
                            )

    def __str__(self):
        return self.name


class Place(ImageModel):
    """
    Place
    """
    name = models.CharField("Nombre del lugar",max_length=512)
    address = models.TextField("Dirección",max_length=2048)
    latitude = models.CharField("Latitud",max_length=50)
    longitude = models.CharField("Longitude",max_length=50)

    def __str__(self):
        return self.name


class Service(ImageModel):

    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="services")
    name = models.CharField(verbose_name="Nombre del servicio",max_length=255)
    origin = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,default=None,verbose_name="Lugar de partida",related_name="service_origin")
    destination = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,default=None,verbose_name="Lugar de Destino",related_name="service_destination")
    price = models.IntegerField(verbose_name="Costo del viaje por persona (Bolivianos)")
    description = models.TextField(verbose_name="Descripcion del Servicio",max_length=4096)

    def __str__(self):
        return self.name

class Travel(models.Model):
    str_type_travel = {
        'I': 'Solo ida',
        'V': 'Ida y vuelta',
    }

    TYPE_TRAVEL = {
        ('I', 'Solo ida'),
        ('V','Ida y vuelta'),
    }

    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    time_departure = models.DateTimeField()
    time_arrival_destination = models.DateTimeField()
    time_departure_return = models.DateTimeField(null=True, default=None)
    time_arrival_return = models.DateTimeField(null=True, default=None)
    travel_type = models.CharField(max_length=1, choices=TYPE_TRAVEL)

    travelers = models.ManyToManyField(
        Customer,
        through='Traveler',
        through_fields=('travel', 'customer'),
        related_name="travel_registered"

    )
    bookers = models.ManyToManyField(
        Customer,
        through='Booker',
        through_fields=('travel', 'customer'),
        related_name = "travel_reserved"
    )
    available_seats = models.PositiveSmallIntegerField(default=1)

    passengers_limit = models.PositiveIntegerField(
        default=0,
        help_text='If travel is limited, this will be the limit on the number of members.'
    )

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities.'
    )

    rating = models.FloatField(null=True)

    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Used for disabling the ride or marking it as finished.'
    )

    def __str__(self):
        """Return travel details."""

        return '{_from} a {to} | {day} {i_time} - {day_arrival} {f_time}'.format(
            _from=self.service.origin,
            to=self.service.destination,
            day=self.time_departure.strftime('%a %d, %b'),
            i_time=self.time_departure.strftime('%I:%M %p'),
            day_arrival=self.time_arrival_return.strftime('%a %d, %b'),
            f_time=self.time_arrival_return.strftime('%I:%M %p'),
        )


class Traveler(models.Model):
    """Traveler model."""
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
    rating = models.FloatField(null=True)

    def __str__(self):
        """Return username and travel info."""
        return '{},{},{}'.format(
            self.customer.full_name,
            self.travel.id,
            self.travel.service
        )

class Booker(models.Model):
    """Booker model."""
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
    taked = models.BooleanField(default=False)

    def __str__(self):
        """Return username and travel info."""
        return '{},{},{}'.format(
            self.customer.full_name,
            self.travel.id,
            self.travel.service
        )