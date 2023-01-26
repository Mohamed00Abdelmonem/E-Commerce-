from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Electronics', views.Electronics, name='products'),
    path('about', views.about, name='about'),
    path('Furniture', views.Furniture, name='furniture'),
    path('Clothes', views.Clothes, name='clothes'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

