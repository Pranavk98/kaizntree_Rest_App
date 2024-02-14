from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item, Category, Tag
from django.utils import timezone

class ItemAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data for Category and Tag
        cls.category = Category.objects.create(name="Electronics")
        cls.tag = Tag.objects.create(name="Portable")
        cls.item = Item.objects.create(
            sku="WAT",
            name="Watch",
            category=cls.category,
            stock_status="In Stock",
            available_stock=15,
            created_at=timezone.now()
        )
        cls.item.tags.add(cls.tag)

    def test_create_item(self):
        """
        Ensure we can create a new item object, specifying category by ID.
        """
        url = reverse('item-list')
        data = {
            "sku": "MIC",
            "name": "Microphone",
            "stock_status": "Out of Stock",
            "available_stock": 0,
            "category_id": self.category.id,  # Now passing category_id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)
        item = Item.objects.latest('id')
        self.assertEqual(item.name, "Microphone")
        self.assertEqual(item.category, self.category)  # Verifying category was set correctly


    def test_get_item_list(self):
        """
        Ensure we can retrieve a list of items.
        """
        url = reverse('item-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming no pagination

    def test_filter_items_by_stock_status(self):
        """
        Ensure we can filter items by stock status.
        """
        url = f"{reverse('item-list')}?stock_status=In+Stock"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(item['stock_status'] == "In Stock" for item in response.data))
