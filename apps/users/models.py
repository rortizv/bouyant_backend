from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, phone_number, address, country, doc_type, doc_number, born_date, is_owner, ships, reviews, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            country=country,
            doc_type=doc_type,
            doc_number=doc_number,
            born_date=born_date,
            is_owner=is_owner,
            ships=ships,
            reviews=reviews,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, phone_number, address, country, doc_type, doc_number, born_date, is_owner, ships, reviews, **extra_fields):
        return self._create_user(email, password, first_name, last_name, phone_number, address, country, doc_type, doc_number, born_date, is_owner, ships, reviews, False, False, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, phone_number, address, country, doc_type, doc_number, born_date, **extra_fields):
        return self._create_user(email, password, first_name, last_name, phone_number, address, country, doc_type, doc_number, born_date, True, True, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=255, unique=True)
    first_name = models.CharField('First name', max_length=255)
    last_name = models.CharField('Last name', max_length=255)
    phone_number = models.CharField('Phone number', max_length=255)
    doc_type = models.CharField('Document type', max_length=255)
    doc_number = models.CharField('Document id', max_length=255)
    address = models.CharField('Address', max_length=255)
    country = models.CharField('Country', max_length=255)
    born_date = models.DateField()
    is_owner = models.BooleanField(default=False)
    ships = models.TextField('Ships', null=True, blank=True)
    reviews = models.TextField('Reviews', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    history = HistoricalRecords()

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'country', 'doc_type', 'doc_number', 'address', 'born_date']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'