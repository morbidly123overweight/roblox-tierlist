"""
URL configuration for robloxt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from robloxt import views

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('register/', views.register_view, name='register'),    # Registrácia nového používateľa
    path('login/', views.login_view, name='login'),            # Prihlásenie
    path('logout/', views.logout_view, name='logout'),         # Odhlásenie
    
    # Game management URLs
    path('', views.hry_list_view, name='hry_list'),           # Hlavná stránka so zoznamom hier
    path('pridat-hru/', views.pridat_hru_view, name='pridat_hru'),  # Pridanie novej hry
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
