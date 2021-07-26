from django.urls import include,path
from . import views

urlpatterns = [
    path('registration/', views.registration, name = 'registration'),
    path('edit_user/<int:id>/', views.edit_user, name = 'edi_user'),
    path('add_product/', views.add_product, name = 'add_product'), 
]