from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Product, Category, Brand, Favorite


class AddToFavoritesViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product')

    def test_add_to_favorites_with_authenticated_user(self):
        response = self.client.post(reverse('add_to_favorites', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Favorite.objects.filter(user=self.user, product=self.product).exists())

    def test_add_to_favorites_redirects_to_favorites_page(self):
        response = self.client.post(reverse('add_to_favorites', args=[self.product.id]))
        self.assertRedirects(response, reverse('favorites'))

    def test_add_to_favorites_with_unauthenticated_user(self):
        self.client.logout()
        response = self.client.post(reverse('add_to_favorites', args=[self.product.id]))
        self.assertNotEqual(response.status_code, 200)

    def test_add_to_favorites_with_nonexistent_product(self):
        response = self.client.post(reverse('add_to_favorites', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_add_to_favorites_prevents_duplicate(self):
        Favorite.objects.create(user=self.user, product=self.product)
        response = self.client.post(reverse('add_to_favorites', args=[self.product.id]))
        self.assertEqual(Favorite.objects.filter(user=self.user, product=self.product).count(), 1)
