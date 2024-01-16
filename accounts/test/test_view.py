from django.test import Client, TestCase
from django.urls import reverse
from accounts.models import User

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:register')
    
    def test_register_ok(self):
        data = {'username': 'test', 
                'password1':'test123', 
                'password2':'test123',
                'email': 'test@test.com'}
        response = self.client.post(self.register_url, data)
        index_url = reverse('home')
        self.assertRedirects(response, index_url,)
        self.assertEquals(User.objects.count(), 1)
    
    def test_register_error(self):
        data = {'username': 'test', 
                'password1':'test123', 
                'password2':'test123'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response,'form','email','esse campo ...')
        
