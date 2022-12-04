from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Domain(models.Model):

    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SubDomain(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)

    url = models.URLField(verbose_name="Website")

    address = models.CharField(verbose_name="Address",  max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, null=True, default=None)
    subdomain = models.ForeignKey(SubDomain, on_delete=models.DO_NOTHING, blank=True, default=None, null=True)

    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    age = models.IntegerField(verbose_name="Age", default=40)
    net_worth = models.IntegerField(verbose_name="Net Worth($100K)", default=100)

    def __str__(self):
        return self.name



