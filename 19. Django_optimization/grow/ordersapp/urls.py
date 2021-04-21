from django.urls import path
import ordersapp.views as ordersapp


app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.ListOrder.as_view(), name='index'),
    path('create/', ordersapp.CreateOrder.as_view(), name='create_order'),
    path('update/<int:pk>/', ordersapp.UpdateOrder.as_view(), name='update_order'),
    path('order_buy/<int:pk>/', ordersapp.buy_order, name='buy_order'),
    path('read/<int:pk>/', ordersapp.DetailOrder.as_view(), name='read_order'),
    path('delete/<int:pk>/', ordersapp.DeleteOrder.as_view(), name='delete_order'),
]