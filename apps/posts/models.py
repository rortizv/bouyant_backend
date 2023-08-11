from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.ships.models import Ship


class Post(BaseModel):
    title = models.CharField('Title', max_length=255)
    ship_id = models.ForeignKey(Ship, on_delete=models.CASCADE, verbose_name='Ship')
    journey = models.CharField('Journey', max_length=255)
    price = models.IntegerField('Price')
    discount = models.IntegerField('Discount')
    description = models.TextField('Description')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'