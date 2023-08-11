from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.posts.models import Post
from apps.ships.models import Ship
from apps.users.models import User
from apps.reviews.models import Review


class Reservation(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='User')
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, verbose_name='Post')
    ship = models.ForeignKey('ships.Ship', on_delete=models.CASCADE, verbose_name='Ship')
    review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE, verbose_name='Review')
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    journey = models.CharField('Journey', max_length=255)
    total_price = models.IntegerField('Total Price')
    pax = models.IntegerField('Pax')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'{self.user} - {self.post} - {self.ship} - {self.review} - {self.start_date} - {self.end_date} - {self.journey} - {self.total_price} - {self.pax}'