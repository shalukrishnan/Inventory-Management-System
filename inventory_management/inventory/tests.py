from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import InventoryItem

class InventoryTests(APITestCase):
    def test_create_item(self):
        url = reverse('inventoryitem-list')
        data = {'name': 'Item1', 'description': 'Item description', 'quantity': 10, 'price': 100.0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
