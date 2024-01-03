from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
# Create your tests here.
class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('commerce:home')

    def tearDown(self):
        pass
    
    def test_status_code(self):
        reponse = self.client.get(self.url)
        self.assertEqual(reponse.status_code,200)
    
    def test_templete_used(self):
        reponse = self.client.get(self.url)
        self.assertTemplateUsed(reponse, 'index.html')

class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('commerce:contact')

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    # def test_form_error(self):
    #     data = {'name':'', 'message':'', 'email':''}
    #     response = self.client.post(self.url, data)
    #     # self.assertFormError(response,'form','name','')
    #     self.assertFormError(response,'form','email','Enter a valid email address.')
    #     # self.assertFormError(response,'form','message','This field is required.')

    def test_form_ok(self):
        data = {'name':'test', 'message':'test', 'email':'test@test.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox),1)
        self.assertEquals(mail.outbox[0].subject,'Contato E-commerce')
        
        
