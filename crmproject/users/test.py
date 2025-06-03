from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order,CustomUser

User = get_user_model()
class OrderViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.customer_user = CustomUser.objects.create_user(
            username='customer1',
            password='testpass123',
            user_type='customer'
        )

        self.subscriber_user = CustomUser.objects.create_user(
            username='subscriber1',
            password='testpass123',
            user_type='subscriber'
        )

    def test_customer_can_create_order(self):
        self.client.login(username='customer1', password='testpass123')
        response = self.client.post(reverse('create_order'), {
            'product_name': 'Test Product',
            'amount': '99.99',
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Order.objects.count(), 1)

    def test_subscriber_cannot_create_order(self):
        self.client.login(username='subscriber1', password='testpass123')
        response = self.client.post(reverse('create_order'), {
            'product_name': 'Test Product',
            'amount': '99.99',
            'status': 'pending'
        })
        self.assertNotEqual(Order.objects.count(), 1)
        self.assertIn(response.status_code, [302, 403])

    def test_order_visible_to_customer(self):
        order = Order.objects.create(
            customer=self.customer_user,
            product_name='Demo Product',
            amount=150.00,
            status='pending'
        )
        self.client.login(username='customer1', password='testpass123')
        response = self.client.get(reverse('view_orders'))
        self.assertContains(response, 'Demo Product')