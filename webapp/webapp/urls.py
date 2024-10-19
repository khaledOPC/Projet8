from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.shortcuts import redirect

import webpage
import users
from webpage import views
from users import views
from users.views import add_to_favorites, favorites

# Personnalisation de la vue de déconnexion pour gérer les redirections et afficher un message.
def custom_logout_view(request):
    if request.user.is_authenticated:
        auth_views.LogoutView.as_view()(request)
    else:
        messages.error(request, "Vous devez vous connecter pour pouvoir vous déconnecter.")
    return redirect('home')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('base/', webpage.views.base, name='base'),
    path('', users.views.home, name='home'),
    path('signup/', users.views.signup, name='signup'),
    path('resultat/', users.views.resultat, name='resultat'),
    path('Connected/', users.views.Connected, name='Connected'),
    path('search/', views.search, name='search'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('substitutes/<int:product_id>/', views.product_substitutes, name='product_substitutes'),
    path('add_to_favorites/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/', favorites, name='favorites'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', custom_logout_view, name='logout'),  # Modification pour la déconnexion personnalisée
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
