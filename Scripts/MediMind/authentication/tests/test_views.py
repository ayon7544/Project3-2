from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_should_show_register_page(self):
        response = self.client.post(reverse("login"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/loginpage.html")
    
    def test_should_show_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/loginpage.html")
    
    def test_should_signup_user(self):
        self.user = {
            "username": "username",
            "email": "test@example.com",
            "password": "password",
            "password2": "password"
        }
        # response = self.client.post(reverse("login"))
        # self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response.status_code, 302)
        
    
    
    