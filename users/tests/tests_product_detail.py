'''import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from users.models import Product, Category, Brand  # Assurez-vous que les modèles sont correctement importés


class ProductPageTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Exécute Chrome en mode sans tête.
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Configure le service Chrome
        chrome_service = ChromeService(ChromeDriverManager().install())

        # Initialise le driver Chrome avec le service et les options
        cls.selenium = webdriver.Chrome(service=chrome_service, options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        # Configure les éléments nécessaires pour le test
        self.category = Category.objects.create(name="Some Category")
        self.brand = Brand.objects.create(name="Some Brand")
        self.product = Product.objects.create(
            name="Test Product",
            nutriscore='A',
            novascore=1,
            category=self.category,
            brand=self.brand,
            # ... autres champs comme l'image, etc. ...
        )

    def test_product_detail(self):
        # Construit l'URL pour la page de détail du produit
        product_detail_url = self.live_server_url + reverse('product_detail', kwargs={'product_id': self.product.id})
        
        # Demande à Selenium d'aller sur cette page
        self.selenium.get(product_detail_url)

        # Utilise Selenium pour rechercher des éléments sur la page et interagir avec eux
        # Par exemple, vérifie que le nom du produit est affiché correctement
        product_name_element = self.selenium.find_element(By.CSS_SELECTOR, "h4.card-title")
        self.assertEqual(product_name_element.text, "Test Product")

# ... the rest of your test class ...

        # Ici, vous pouvez ajouter plus d'interactions ou de vérifications, comme cliquer sur un bouton, remplir un formulaire, etc.

        # NOTE : Assurez-vous que les sélecteurs CSS/ID/Class utilisés pour trouver des éléments correspondent à ceux de votre code HTML réel.

'''