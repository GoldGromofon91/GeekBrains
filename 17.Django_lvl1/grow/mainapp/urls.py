from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('category/', mainapp.house_grow, name='category'),
    path('category/<int:pk>/', mainapp.house_grow_products, name='self_category')
]