"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import webpage
import users
from webpage import views
from users import views
from users.views import add_to_favorites, favorites


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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)