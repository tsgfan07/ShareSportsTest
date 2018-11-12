from django.db import models
from .choices import *
from django.contrib.auth.models import User
from django.conf import settings
import geopy
from geopy.geocoders import Nominatim

class Article(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images', default=str('None/no-img.jpg'))
    contact_email= models.CharField(max_length=140)
    contact_phone= models.CharField(max_length=140)
    category = models.IntegerField(choices=STATUS_CHOICES, default=1)
    #tags = TaggableManager()
    location = models.TextField(max_length=140, default="76131 Karlsruhe")
    location_longitude = models.DecimalField(max_digits=20, decimal_places=15, default="48.5")
    location_latitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.title


    def calculate_location(self):
        gmaps = GoogleMaps("AIzaSyCWVFMuIcrCZ90YUGvyhy6fbkfcRIC8lJU")
        result= gmaps.geocode(location)
        placemark = results['Placemark'][0]
        details = placemark['AddressDetails']['Country']['AdministrativeArea']
        city=details['Locality']['LocalityName']
        return city


    def geo_location(self):
        try:
            geolocator = Nominatim(user_agent="gearshare2018")
            geopy.geocoders.options.default_format_string = '%s Deutschland'
            city = geolocator.geocode(self.location, timeout=50)
        except GeocoderTimedOut:
            city="Schückstrasse 2, 76131 Karlsruhe"
        return city