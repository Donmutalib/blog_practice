from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from blog_practice_app.models import Blog

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="abdulrahman", password='1Aa@14105810')
        self.client.login(username='abdulrahman', password='1Aa@14105810')
        self.object = Blog.objects.create(
            text = 'test text',
            title = 'test title')
            

    def test_home(self):

        response = self.client.get(reverse('blog_practice_app:index'))
        self.assertEquals(response.status_code, 200)


    def test_list_url(self):
        
        response = self.client.get(reverse('blog_practice_app:blogs'))
        self.assertEquals(response.status_code, 200)


    def test_detail_url(self):

        response = self.client.get(reverse('blog_practice_app:blog', kwargs={'pk': self.object.pk}))
        self.assertEquals(response.status_code, 200)


    def test_create(self):

        data = {
            'title': 'Created title',
            'text': 'Created text'
        }

        response = self.client.post(reverse('blog_practice_app:blog_create'), data)
        self.assertEqual(response.status_code, 302)
        

    def test_update(self):

        response = self.client.post(
            reverse('blog_practice_app:blog_update', kwargs={'pk': self.object.pk}),
            {'text': 'new text', 'title': 'new title'})

        self.assertEqual(response.status_code, 302)



    # def test_update(self):

    #     response = self.client.get(reverse('blog_practice_app:blog_update', kwargs={'pk': self.object.pk}))
    #     self.assertEquals(response.status_code, 200)


    def test_delete(self):

        response = self.client.post(reverse('blog_practice_app:blog_delete', kwargs={'pk': self.object.pk}))
        self.assertEquals(response.status_code, 302)


