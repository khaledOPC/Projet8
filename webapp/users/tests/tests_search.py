from django.test import TestCase, Client
from django.urls import reverse
from users.models import Product, Category
from django.db.models import Q

class SearchViewTestCase(TestCase):

    def setUp(self):
        # Initialisation du client de test
        self.client = Client()
        
        # Initialisation des catégories et des produits
        self.category = Category.objects.create(name='Test Category')
        
        self.products = [
            Product.objects.create(name=f'Test Product {i}', category=self.category, nutriscore='A', novascore='1') 
            for i in range(55)  # Création de 55 produits pour tester la limite de 50
        ]
        
        # URL de la vue à tester
        self.search_url = reverse('search')
        
    def test_search_view_uses_correct_template(self):
        response = self.client.get(self.search_url, {'query': 'Test'})
        self.assertTemplateUsed(response, 'search.html')
        
    def test_search_view_with_query(self):
        response = self.client.get(self.search_url, {'query': 'Test'})
        self.assertEqual(len(response.context['results']), 50)  # La limite doit être de 50
        self.assertIn(self.products[0], response.context['results'])
        
    def test_search_view_without_query(self):
        response = self.client.get(self.search_url)
        self.assertEqual(len(response.context['results']), 50)  # La limite doit être de 50
        self.assertIn(self.products[0], response.context['results'])
        
    def test_search_view_results_limit(self):
        response = self.client.get(self.search_url, {'query': 'Test'})
        self.assertEqual(len(response.context['results']), 50)  # La limite doit être de 50
    

    def test_search_view_products_with_substitutes(self):
        category = Category.objects.create(name='TestCategory')
        
        original_product = Product.objects.create(
            name='Original Product', category=category, nutriscore='D', novascore='4')
        
        substitute_product = Product.objects.create(
            name='Substitute Product', category=category, nutriscore='B', novascore='4')
        
        non_substitute_product = Product.objects.create(
            name='Non Substitute Product', category=category, nutriscore='A', novascore='1')
        
        response = self.client.get(reverse('search'), {'query': 'Original'})
        
        self.assertTrue(original_product.substitutes_exists())
        
        substitutes_exist_for_non_substitute = Product.objects.filter(
            category=non_substitute_product.category
        ).exclude(id=non_substitute_product.id).filter(
            Q(nutriscore__lt=non_substitute_product.nutriscore) | Q(novascore__lt=non_substitute_product.novascore)
        ).exists()
        
        self.assertFalse(substitutes_exist_for_non_substitute)

