from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass
    
    def test_status_code(self):
        reponse = self.client.get(self.url)
        self.assertEqual(reponse.status_code,200)
    
    def test_templete_used(self):
        reponse = self.client.get(self.url)
        self.assertTemplateUsed(reponse, 'index.html')

