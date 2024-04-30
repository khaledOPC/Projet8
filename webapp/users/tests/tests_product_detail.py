from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Ajouté
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from users.models import Product, Category, Brand
from django.contrib.auth.models import User
# Vos modèles personnalisés (remplacez 'YourApp' et 'YourModel' par les noms appropriés)

class ProductPageTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.

        # Set up the Chrome service
        chrome_service = Service(ChromeDriverManager().install())

        # Now initialize the Chrome driver with the service
        cls.selenium = webdriver.Chrome(service=chrome_service, options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        # Set up the necessary elements for the test
        self.category = Category.objects.create(name="Some Category")
        self.brand = Brand.objects.create(name="Some Brand")
        self.product = Product.objects.create(
            name="Test Product",
            nutriscore='A',
            novascore=1,
            category=self.category,
            brand=self.brand,
            # ... other fields such as image, etc. ...
        )

    def test_product_detail(self):
        # Construct the URL for the product detail page
        product_detail_url = self.live_server_url + reverse('product_detail', kwargs={'product_id': self.product.id})
        
        # Tell Selenium to go to that page
        self.selenium.get(product_detail_url)

        # Now, use Selenium to look for elements on the page and interact with them
        # For example, verify that the product name is displayed correctly
        product_name_element = self.selenium.find_element(By.CSS_SELECTOR, "h4.card-title")
        self.assertEqual(product_name_element.text, "Test Product")

# ... the rest of your test class ...


        # Ici, vous pouvez ajouter plus d'interactions ou de vérifications, comme cliquer sur un bouton, remplir un formulaire, etc.

        # NOTE : Assurez-vous que les sélecteurs CSS/ID/Class utilisés pour trouver des éléments correspondent à ceux de votre code HTML réel.



'''
Test fonctionnel comme un parcour connexion , recherche sauvegarde etc..
Pas oblgié de chercher une page on peut chercher à cliquer sur un bouton ou un
lien par exemple
Eviter de toucher à la BDD
'''



'''
tester qu'on est bien connecter et qu'on puisse bien s'inscire avec 'mon compte' 
Supprimer l'utilisateur pour clean et pas avoir un compte deja existant quand on
test encore

'''