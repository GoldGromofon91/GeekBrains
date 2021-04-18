from django.urls import path
import ordersapp.views as ordersapp


app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='index'),
    path('create/', ordersapp.CreateOrder.as_view(), name='create_order'),
    path('update/<int:pk>/', ordersapp.UpdateOrder.as_view(), name='update_order'),
    path('order_buy/<int:pk>/', ordersapp.buy_order, name='buy_order'),

]