from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order

User = get_user_model()

class OrderViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = User.objects.create_user(
            username='customeruser',
            password='customerpassword',
            user_type= 'customer'
        )
        self.subscriber = User.objects.create_user(
            username='subscriberuser',
            password='testpass123',
            user_type='subscriber'
        )
        self.admin = User.objects.create_user(
            username='adminuser',
            password='testpass123',
            user_type='superadmin'
        )