from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()  # Ensure this field exists
    phone_number = models.CharField(max_length=15)  # Ensure this field exists

    def __str__(self):
        return self.name

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)  # Assuming Item exists
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # ✅ Make email unique

    # Optional: add any custom fields like phone, user_type, etc.
    phone = models.CharField(max_length=15, blank=True)
    user_type = models.CharField(max_length=10, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # or include first_name, last_name, etc. as needed

    def __str__(self):
        return self.email
