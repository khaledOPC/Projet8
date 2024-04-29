# Dans le fichier ~/Projet8/webapp/management/commands/update_products.py
# your_app/management/commands/update_products.py

import requests
from django.core.management.base import BaseCommand
from users.models import Product, Brand, Category, Store

def get_or_create_brand(name):
    brand, _ = Brand.objects.get_or_create(name=name)
    return brand

def get_or_create_store(name):
    store, _ = Store.objects.get_or_create(name=name)
    return store

def get_or_create_category(name):
    category, _ = Category.objects.get_or_create(name=name)
    return category


class Command(BaseCommand):
    help = 'Update existing products from OpenFoodFacts'


    def handle(self, *args, **options):
        products = Product.objects.all()  # Adjust query as needed
        for product in products:
            self.update_product(product.barcode)

    def update_product(self, barcode):
        response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')
        data = response.json()

        if response.status_code == 200 and data['status'] == 1:
            product_data = data['product']
            product, updated = Product.objects.update_or_create(
                    barcode=barcode,
                    defaults={
                        'name': product_data.get('product_name'),
                        'nutriscore': product_data.get('nutrition_grades'),
                        'nova_group': product_data.get('nova_group'),
                        'url': product_data.get('url'),
                        'brand': get_or_create_brand(product_data.get('brands')),
                        'categories': [get_or_create_category(cat) for cat in product_data.get('categories').split(",") if cat],
                        'stores': [get_or_create_store(store) for store in product_data.get('stores').split(",") if store],
                    }
                )
            if updated:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated product "{product.name}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'No updates were necessary for "{product.name}"'))

