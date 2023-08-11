from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class Ship(BaseModel):
    name = models.CharField('Name', max_length=255)
    registry = models.CharField('Registry', max_length=255)
    owner = models.ForeignKey('ShipOwner', on_delete=models.CASCADE, verbose_name='Ship owner')
    ship_type = models.ForeignKey('ShipType', on_delete=models.CASCADE, verbose_name='Ship type')
    model = models.CharField('Model', max_length=255)
    image = models.ImageField('Image', upload_to='ships', null=True, blank=True)
    pax = models.IntegerField('Pax')
    length = models.IntegerField('Length')
    fabrication_year = models.IntegerField('Fabrication year')
    bathrooms = models.IntegerField('Bathrooms')
    restrooms = models.IntegerField('Restrooms')
    description = models.TextField('Description')
    location = models.CharField('Location', max_length=255)
    reservations = models.TextField('Reservations')
    reviews = models.TextField('Reviews')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Ship'
        verbose_name_plural = 'Ships'

    def __str__(self):
        return f'{self.name} - {self.owner} - {self.ship_type} - {self.pax} - {self.location}'


class ShipType(BaseModel):
    name = models.CharField('Name', max_length=255, unique=True, null = False, blank = False)
    description = models.TextField('Description', null = True, blank = False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Ship type'
        verbose_name_plural = 'Ship types'

    def __str__(self):
        return f'{self.name}'


class ShipOwner(BaseModel):
    name = models.CharField('Name', max_length=255, unique=True, null = False, blank = False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Ship owner'
        verbose_name_plural = 'Ship owners'

    def __str__(self):
        return f'{self.name}'


class ShipAccesories(BaseModel):
    name = models.CharField('Name', max_length=255, unique=True, null = False, blank = False)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Ship accesory'
        verbose_name_plural = 'Ship accesories'

    def __str__(self):
        return f'{self.name}'


class ShipImage(BaseModel):
    ship = models.ForeignKey('Ship', on_delete=models.CASCADE, verbose_name='Ship')
    image = models.ImageField('Image', upload_to='ships', null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Ship image'
        verbose_name_plural = 'Ship images'

    def __str__(self):
        return f'{self.ship} - {self.image}'