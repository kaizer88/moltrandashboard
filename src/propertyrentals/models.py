from django.db import models
from lib.models import BaseModel
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)

    def __str__(self):
        return self.code


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class Property(BaseModel):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    address = models.CharField(max_length=5, unique=True, null=False, blank=False)

    def __str__(self):
        return self.code


class Address(models.Model):

    property = models.ForeignKey(
        'Property', related_name="property_addresses", on_delete=models.CASCADE, null=False, blank=False)
    address_line_one = models.CharField(max_length=255, null=True, blank=True)
    address_line_two = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    town = models.ForeignKey('Town', on_delete=models.CASCADE, null=False, blank=False)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, null=False, blank=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.address_line_one


class Tenant(BaseModel):
    first_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_number = models.CharField(max_length=255, unique=True, null=False, blank=False)
    cell_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    kin_number = models.IntegerField(null=True, blank=True)
    kin_first_name = models.CharField(max_length=30, null=True, blank=True)
    kin_last_name = models.CharField(max_length=30, null=True, blank=True)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, null=False, blank=False, related_name="property_tenant")

    def __str__(self):
        return self.first_name


class Agent(BaseModel):
    first_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    id_number = models.CharField(max_length=255, unique=True, null=False, blank=False)
    cell_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    kin_number = models.IntegerField(null=True, blank=True)
    kin_first_name = models.CharField(max_length=30, null=True, blank=True)
    kin_last_name = models.CharField(max_length=30, null=True, blank=True)
    town = models.ForeignKey('Town', related_name="town_agent", on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    surname = models.CharField(max_length=150, null=False, blank=False)
    initials = models.CharField(max_length=150, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    date_of_birth = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name