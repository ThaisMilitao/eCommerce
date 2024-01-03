from django.test import Client, TestCase
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Category, Product

class ProductListTestCase(TestCase):
    def setUp(self):
        self.url = reverse('catalog:products_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)

    def tearDown(self):
        Product.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'products.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['products']
        self.assertEquals(product_list.count(), 10)