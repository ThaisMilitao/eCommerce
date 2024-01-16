from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from model_mommy import mommy
from django.contrib.auth import get_user_model

User = get_user_model()
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
        

class LoginViewtestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(User)
        self.user.set_password('123')
        self.assertAlmostEqualsuser.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertTrue(not response.wsgi_request.user.is_authenticated())
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'login.html')
        data = {'username': self.user.username, 'password':'123'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse('home')
        self.assertRedirects(response, redirect_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated())

    def test_login_error(self):
        data = {'username': self.user.username, 'password':'1234'}
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        error_msg = {}
        self.assertFormError(response, 'form', None, error_msg)