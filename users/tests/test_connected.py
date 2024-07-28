import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

class ConnectedViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_connected_view_with_unauthenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse('Connected'))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('Connected')}")

    def test_connected_view_uses_correct_template(self):
        response = self.client.get(reverse('Connected'))
        print('Templates used:', response.templates)
        self.assertTemplateUsed(response, 'Connected.html')

    def test_connected_view_context_data(self):
        response = self.client.get(reverse('Connected'))
        print('Context data:', response.context)
        # Ajoutez ici des assertions supplémentaires si nécessaire
