from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User


class TestAuthUrls(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="abdulrahmanew", password='1Aa@14105810')


    def test_register(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('blog_practice_app:register')
        data = {
            'username': 'newuser',
            'password1': '1Aa@14105810',
            'password2': '1Aa@14105810'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


    def testLogin(self):
        data = {
            'username': 'abdulrahmanew',
            'password': '1Aa@14105810'
        }

        response = self.client.post(reverse('blog_practice_app:login'), data)
        self.assertEqual(response.status_code, 302)


    def testLogout(self):

        response = self.client.post(reverse('blog_practice_app:logout'))
        self.assertEqual(response.status_code, 302)




    


    



    

    




