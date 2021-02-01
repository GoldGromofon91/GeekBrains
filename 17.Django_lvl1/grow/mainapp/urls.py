from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.house_grow, name='house_grow'),
    path('<int:pk>/', mainapp.house_grow_products, name='prod')
]