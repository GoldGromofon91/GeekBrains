from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:pk>/', basketapp.add_prod, name='add'),
    path('remove/<int:basket_elem_pk>/', basketapp.remove_prod, name='remove'),

]