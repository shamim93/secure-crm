from django.db import models
from auditlog.registry import auditlog
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('customer', 'Customer'),
        ('subscriber', 'Subscriber'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username
class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name =  models.CharField(max_length=255)
    amount =  models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('processing','Processing'),
        ('shipped', 'Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.product_name} - {self.customer.username}"
    
auditlog.register(Order)
auditlog.register(CustomUser)