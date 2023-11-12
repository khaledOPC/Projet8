import requests
from django.core.management.base import BaseCommand
from users.models import Product, Brand, Category, Store
'''
def insert_brand(name):
    brand, created = Brand.objects.update_or_create(name=name)
    return brand

def insert_category(name):
    category, created = Category.objects.update_or_create(name=name)
    return category

def insert_store(name):
    store, created = Store.objects.update_or_create(name=name)
    return store

class Command(BaseCommand):
    help = 'Import products from OpenFoodFacts API'

    def add_arguments(self, parser):
        parser.add_argument('product_barcodes', nargs='+', type=str)

    def handle(self, *args, **options):
        for barcode in options['product_barcodes']:
            self.import_product(barcode)

    def import_product(self, barcode):
        response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')
        data = response.json()

        if response.status_code == 200 and data['status'] == 1:
            product, created = Product.objects.update_or_create(
                barcode=barcode,
                defaults={
                    'name': data['product']['product_name'],
                    'nutriscore': data['product'].get('nutrition_grades'),
                    'nova_group': data['product'].get('nova_group'),
                    'url': data['product']['url'],
                    'brand': insert_brand(data['product']['brands']),
                    'categories': [insert_category(cat) for cat in data['product']['categories'].split(",")],
                    'stores': [insert_store(store) for store in data['product']['stores'].split(",")],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully imported product "{product.name}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated product "{product.name}"'))

'''

def insert_brand(name):
    brand, created = Brand.objects.update_or_create(name=name)
    return brand

def insert_category(name):
    category, created = Category.objects.update_or_create(name=name)
    return category

def insert_store(name):
    store, created = Store.objects.update_or_create(name=name)
    return store



class Command(BaseCommand):
    

    def add_arguments(self, parser):
        parser.add_argument('product_barcode', type=str)


    def update_or_create_from_barcode(self, barcode):
        response = requests.get(f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json')
        data = response.json()

        if response.status_code == 200 and data['status'] == 1:
            return Product.objects.update_or_create(
                name=data['product']['product_name'],
                defaults={
                    'nutriscore': data['product'].get('nutrition_grades'),
                    'novascore': data['product'].get('novascore'),
                }
            )
        return None, None

    def handle(self, *args, **options):
        barcode = options['product_barcode']
        product, created = self.update_or_create_from_barcode(barcode)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully imported product "{product.name}"'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Successfully updated product "{product.name}"'))