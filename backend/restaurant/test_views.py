from .models import MenuItem
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Banana", price=8, inventory=10)

    def test_getall(self):
        icecream = MenuItem.objects.get(title="IceCream")
        banana = MenuItem.objects.get(title="Banana")
        self.assertEqual(str(icecream), 'IceCream : 80.00')
        self.assertEqual(str(banana), 'Banana : 8.00')
