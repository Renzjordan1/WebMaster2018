from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('buy', views.buy, name='buy'),
    path('search', views.search, name='search'),
    path('school', views.school, name='school'),
    path('image', views.image, name='image'),
    path('course', views.course, name='course'),
    path('teach', views.teach, name='teach'),

    url('tsa', RedirectView.as_view(url='http://manualtsa.com'),
        name='tsa'),

]
