# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cuisinetypes(models.Model):
    cuisine_type_id = models.AutoField(primary_key=True)
    cuisine_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.cuisine_name

    class Meta:
        db_table = 'CuisineTypes'


class Menucategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    menu_type = models.ForeignKey('Menutypes', models.DO_NOTHING)
    category_name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'MenuCategories'


class Menuitems(models.Model):
    menu_item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurants', models.DO_NOTHING)
    category = models.ForeignKey(Menucategories, models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'MenuItems'


class Menutypes(models.Model):
    menu_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'MenuTypes'


class Operatinghours(models.Model):
    hour_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurants', models.DO_NOTHING)
    day_of_week = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        db_table = 'OperatingHours'


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurants', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    rating_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Ratings'


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    restaurant = models.ForeignKey('Restaurants', models.DO_NOTHING)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length=50)
    special_requests = models.TextField(blank=True, null=True)
    booking_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Reservations'


class Restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    price_level = models.CharField(max_length=4)
    cuisine_type = models.ForeignKey(Cuisinetypes, models.DO_NOTHING)

    class Meta:
        db_table = 'Restaurants'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)
    registration_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Users'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
