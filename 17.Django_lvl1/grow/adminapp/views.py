from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from adminapp.forms import GrowAdminChangeForm, GrowCategoryAdminCreateForm, GrowProductsAdminCreateForm

from django.urls import reverse, reverse_lazy

from authapp.forms import GrowUserCreationForm
from mainapp.models import GrowCategory, GrowProducts


class OnlyAdminMixin:
    @method_decorator(user_passes_test(lambda usr: usr.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    key = 'title_page'
    title_page = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.key] = self.title_page
        return context


class GrowUserList(OnlyAdminMixin, PageTitleMixin, ListView):
    model = get_user_model()
    title_page = 'админка->пользователи'


class GrowUserCreate(OnlyAdminMixin, PageTitleMixin, CreateView):
    model = get_user_model()
    form_class = GrowUserCreationForm
    success_url = reverse_lazy('adminapp:index')
    title_page = 'админка->пользователь->создать'


class GrowUserUpdate(OnlyAdminMixin, PageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = GrowAdminChangeForm
    success_url = reverse_lazy('adminapp:index')
    pk_url_kwarg = 'usr_pk'
    title_page = 'админка->пользователи->обновить'


class GrowUserDelete(OnlyAdminMixin, PageTitleMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('adminapp:index')
    title_page = 'админка->пользователи->удаление'
    pk_url_kwarg = "usr_pk"


# @user_passes_test(lambda usr: usr.is_superuser)
# def delete_usr(request, usr_pk):
#     user_obj = get_object_or_404(get_user_model(), pk=usr_pk)
#
#     if not user_obj.is_active or request.method == 'POST':
#         if user_obj.is_active:
#             user_obj.is_active = False
#             user_obj.save()
#         return HttpResponseRedirect(reverse('adminapp:index'))
#     content = {
#         'title_page': 'админка->пользователи->удаление',
#         'user_to_delete': user_obj
#     }
#     return render(request, 'adminapp/growuser_confirm_delete.html', context=content)


class GrowCategoryDelete(OnlyAdminMixin, PageTitleMixin, DeleteView):
    model = GrowCategory
    success_url = reverse_lazy('adminapp:categories')
    title_page = 'админка->категории->удаление'
    pk_url_kwarg = "cat_pk"


class GrowCategoryCreate(OnlyAdminMixin, PageTitleMixin, CreateView):
    model = GrowCategory
    form_class = GrowCategoryAdminCreateForm
    success_url = reverse_lazy('adminapp:categories')
    title_page = 'админка->категории->создать'


class GrowCategoryUpdate(OnlyAdminMixin, PageTitleMixin, UpdateView):
    model = GrowCategory
    form_class = GrowCategoryAdminCreateForm
    success_url = reverse_lazy('adminapp:categories')
    title_page = 'админка->категории->обновить'


class GrowCategoriesList(OnlyAdminMixin, PageTitleMixin, ListView):
    model = GrowCategory
    title_page = 'админка->категории'


@user_passes_test(lambda u: u.is_superuser)
def get_all_products_in_category(request, cat_pk):
    category = get_object_or_404(GrowCategory, pk=cat_pk)
    product_category = category.growproducts_set.all()
    context = {
        'title_page': f'категория {category.name}',
        'category': category,
        'product_in': product_category
    }
    return render(request, 'mainapp/category_products_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_product_create(request, cat_pk):
    category = get_object_or_404(GrowCategory, pk=cat_pk)
    if request.method == 'POST':
        form = GrowProductsAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:products_in_category', kwargs={'cat_pk': category.pk}))
    else:
        form = GrowProductsAdminCreateForm(
            initial={
                'category': category,
            }
        )

    context = {
        'page_title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'mainapp/product_update.html', context)


class GrowProductDetail(OnlyAdminMixin, PageTitleMixin, DetailView):
    model = GrowProducts
    title_page = 'админка->продукт-инфо'
