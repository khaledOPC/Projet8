# Importation des modules nécessaires de Django et autres bibliothèques
from django.shortcuts import render, redirect
from django import forms
import requests
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Favorite, Product

def home(request):
    """
    Vue pour la page d'accueil.
    Affiche simplement la page d'accueil lorsqu'aucune action supplémentaire n'est nécessaire.
    """
    return render(request, 'home.html',)


def search(request):
    """
    Vue pour la recherche de produits.
    Exécute une recherche sur les produits basée sur la requête de l'utilisateur, puis renvoie les résultats.
    Si aucun mot-clé n'est fourni, renvoie tous les produits.
    """
    query = request.GET.get('query')  # Extraction de la requête de recherche de l'utilisateur
    if query:
        results = Product.objects.filter(name__icontains=query)  # Recherche des produits correspondant à la requête
    else:
        results = Product.objects.all()  # Si aucune requête n'est fournie, renvoie tous les produits
    results = results[:50]  # Limite les résultats à 50 produits
    products_with_substitutes = []  # Liste pour stocker les produits ayant des substituts disponibles
    for product in results:  # Pour chaque produit dans les résultats
        if product.nutriscore is not None and product.novascore is not None:  # Si le produit a des scores nutritionnels
            # Recherche des produits substituts et ajout à la liste si existant
            if product.substitutes_exists():
                products_with_substitutes.append(product.id)    
    return render(request, 'search.html', {'results': results, 'products_with_substitutes': products_with_substitutes})



@login_required
def Connected(request):
    """
    Vue pour la page lorsque l'utilisateur est connecté.    
    Sert à afficher une page spécifique ou des informations spécifiques lorsque l'utilisateur est connecté.
    """
    return render(request, 'Connected.html')


def product_detail(request, product_id):
    """
    Vue pour afficher le détail d'un produit spécifique.
    Renvoie les détails d'un produit spécifique basé sur son ID.
    """
    product = get_object_or_404(Product, id=product_id)  # Récupération du produit basé sur l'ID
    if product.nutrition_data:  # Si le produit a des données nutritionnelles
        nutrition = product.nutrition_data  # Récupération des données nutritionnelles
    else:
        nutrition = None  # Si aucune donnée nutritionnelle, assignation à None
    context = {
        'product': product,  # Assignation du produit au contexte
        'nutrition_data': nutrition  # Assignation des données nutritionnelles au contexte
    }
    return render(request, 'product_detail.html', context)


def product_substitutes(request, product_id):
    """
    Vue pour trouver et afficher les substituts d'un produit spécifique.
    Recherche des produits substituts basés sur les scores nutritionnels et la catégorie, puis les renvoie.
    """
    product = get_object_or_404(Product, id=product_id)  # Récupération du produit basé sur l'ID
    if product.nutriscore is None or product.novascore is None:  # Si le produit n'a pas de scores nutritionnels
        context = {'substitutes': []}  # Assignation de substituts vides au contexte
        return render(request, 'substitutes.html', context)  # Renvoie la page avec aucun substitut
    substitutes = Product.objects.filter(category=product.category).exclude(id=product_id).filter(
        Q(nutriscore__lt=product.nutriscore) | Q(novascore__lt=product.novascore)).order_by('nutriscore','novascore')[:10]  
    # Recherche de substituts et ordonnancement par scores
    context = {'substitutes': substitutes}  # Assignation des substituts au contexte
    return render(request, 'substitutes.html', context)  # Renvoie la page avec les substituts trouvés



# Vue pour traiter le formulaire sur la page d'accueil
def button(request):
    """
    Gère le formulaire sur la page d'accueil.
    Si le formulaire est valide, traite les données du formulaire et effectue les actions nécessaires.
    """
    if request.method == 'POST':
        formulaire = MonFormulaire(request.POST)
        if formulaire.is_valid():
            champ_texte = formulaire.cleaned_data['champ_texte']
    else:
        formulaire = MonFormulaire()
    return render(request, 'home.html', {'formulaire': formulaire})

# Vue pour gérer la connexion des utilisateurs
def resultat(request):
    """
    Gère la connexion des utilisateurs.
    Authentifie les utilisateurs basé sur le nom d'utilisateur et le mot de passe fournis, 
    et si l'authentification réussit, l'utilisateur est redirigé vers la page d'accueil.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'resultat.html', {'form': form})

# Vue pour gérer l'inscription des utilisateurs
def signup(request):
    """
    Gère l'inscription des utilisateurs.
    Crée un nouvel utilisateur avec les données fournies, 
    et si l'inscription est réussie, connecte l'utilisateur et le redirige vers la page d'accueil.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('favorites')


@login_required
def favorites(request):
    user_favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': user_favorites})
