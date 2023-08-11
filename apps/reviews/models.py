from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User
from apps.ships.models import Ship
from apps.posts.models import Post
from simple_history.models import HistoricalRecords


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.comment} - {self.rating}'