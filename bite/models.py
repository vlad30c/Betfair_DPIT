from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User

class MyAppUser( models.Model ) :
    def __unicode__( self ) :
       return self.user.username

    phone_number = models.CharField( max_length = 135, blank = True )


class Tags(models.Model):
    CATEGORY_CHOICES = [
        ("cuisine", "Cuisine"),
        ("setting", "Setting"),
    ]

    tag_id = models.AutoField(primary_key=True)  # explicit ID
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        db_table = "Tags"

    def __str__(self):
        return self.name


class Restaurants(models.Model):
    PRICE_LEVEL_CHOICES = [
        ('budget-friendly', 'Budget-friendly'),
        ('average', 'Average'),
        ('expensive', 'Expensive'),
    ]

    restaurant_id = models.AutoField(primary_key=True)  # explicit ID
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    price_level = models.CharField(max_length=20, choices=PRICE_LEVEL_CHOICES)

    tags = models.ManyToManyField(Tags, related_name="restaurants")

    class Meta:
        db_table = "Restaurants"
        constraints = [
            models.CheckConstraint(
                check=Q(price_level__in=['budget-friendly', 'average', 'expensive']),
                name='valid_price_level',
            ),
        ]

    def __str__(self):
        return self.name


class RestaurantSchedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)  # explicit ID
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20)  # "Monday", etc.
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        db_table = "RestaurantSchedules"


class RestaurantFiles(models.Model):
    file_id = models.AutoField(primary_key=True)  # explicit ID
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    file_url = models.URLField()
    type = models.CharField(max_length=50)  # "menu" or "photo"
    uploaded_at_utc = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "RestaurantFiles"


class Menutypes(models.Model):
    menu_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'MenuTypes'

    def __str__(self):
        return self.type_name


class Menucategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    menu_type = models.ForeignKey(Menutypes, on_delete=models.DO_NOTHING)
    category_name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'MenuCategories'

    def __str__(self):
        return self.category_name


class Menuitems(models.Model):
    menu_item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurants', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Menucategories, on_delete=models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'MenuItems'

    def __str__(self):
        return self.item_name


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    rating_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Ratings'

    def __str__(self):
        return f"{self.restaurant} - {self.user} ({self.score})"


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurants', on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.IntegerField()
    status = models.CharField(max_length=50)
    special_requests = models.TextField(blank=True, null=True)
    booking_timestamp = models.DateTimeField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'Reservations'

    def __str__(self):
        return f"{self.user} → {self.restaurant} on {self.reservation_date}"
