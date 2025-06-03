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
    def test_customer_can_create_order(self):
        self.client.login(username='customeruser', password='testpass123')

        response = self.client.post(reverse('create_order'), {
            'title': 'Test Order',
            'description': 'A test order',
            'status': 'Pending',
        })

        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().customer, self.customer)

    def test_subscriber_cannot_create_order(self):
        self.client.login(username='subscriberuser', password='testpass123')

        response = self.client.get(reverse('create_order'))
        self.assertEqual(response.status_code, 302) 

    def test_order_visible_to_customer(self):
        Order.objects.create(
            customer=self.customer,
            title='Visible Order',
            description='Should be visible',
            status='Pending'
        )

        self.client.login(username='customeruser', password='testpass123')
        response = self.client.get(reverse('view_orders'))

        self.assertContains(response, 'Visible Order')

    def test_order_not_visible_to_subscriber(self):
        self.client.login(username='subscriberuser', password='testpass123')
        response = self.client.get(reverse('view_orders'))
        self.assertEqual(response.status_code, 302) 