from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class SpecialService(BaseModel):
    name: models.CharField = models.CharField('Name', max_length=255, unique=True, null = False, blank = False)
    description: models.TextField = models.TextField('Description', max_length=255, null = True, blank = False)
    price: models.DecimalField = models.DecimalField('Price', max_digits=10, decimal_places=0, null = True, blank = False)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Special Service'
        verbose_name_plural = 'Special Services'

    def __str__(self):
        return f'{self.name} - {self.description} - {self.price}'