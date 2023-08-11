from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_at = models.DateTimeField('Created at', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField('Deleted at', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'