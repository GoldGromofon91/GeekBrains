from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.GrowUserList.as_view(), name='index'),
    path('user/create/', adminapp.GrowUserCreate.as_view(), name='user_create'),
    path('user/delete/<int:usr_pk>/', adminapp.GrowUserDelete.as_view(), name='user_delete'),
    path('user/update/<int:usr_pk>/', adminapp.GrowUserUpdate.as_view(), name='user_update'),


    path('categories/', adminapp.GrowCategoriesList.as_view(), name='categories'),
    path('category/create/', adminapp.GrowCategoryCreate.as_view(), name='categories_create'),
    path('category/update/<int:pk>', adminapp.GrowCategoryUpdate.as_view(), name='categories_update'),
    path('category/delete/<int:cat_pk>', adminapp.GrowCategoryDelete.as_view(), name='categories_delete'),

    path('category/<int:cat_pk>/products/', adminapp.get_all_products_in_category, name='products_in_category'),
    path('category/<int:cat_pk>/product/create', adminapp.category_product_create, name='category_product_create'),


    path('product/info/<int:pk>/', adminapp.GrowProductDetail.as_view(), name='product_detail'),

]