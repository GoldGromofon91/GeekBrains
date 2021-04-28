from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from ordersapp.forms import OrderForm, OrderItemForm
from ordersapp.models import Order, ItemInOrder


class LoginUserOnlyMixin:
    @method_decorator(user_passes_test(lambda user: user.is_authenticated))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ListOrder(LoginUserOnlyMixin, ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrder(LoginUserOnlyMixin,CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        OrdersFormSet = inlineformset_factory(Order, ItemInOrder, form=OrderItemForm, extra=3)

        if self.request.POST:
            formset = OrdersFormSet(self.request.POST, self.request.FILES)
        else:
            context['form'].initial['user'] = self.request.user
            basket_items = self.request.user.basket.all()
            if basket_items and basket_items.count():
                OrdersFormSet = inlineformset_factory(Order, ItemInOrder,
                                                      form=OrderItemForm,
                                                      extra=basket_items.count() + 1)
                formset = OrdersFormSet()

                for form, basket_items in zip(formset.forms, basket_items):
                    form.initial['product'] = basket_items.product
                    form.initial['count'] = basket_items.count
            else:
                formset = OrdersFormSet()
        context['item_in_order'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['item_in_order']

        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
                self.request.user.basket.all().delete()

        if self.object.summary_product['total_cost'] == 0.00:
            self.object.delete()

        print(self.object.summary_product['total_cost'])
        return order


class UpdateOrder(LoginUserOnlyMixin,UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(
            Order, ItemInOrder, form=OrderItemForm, extra=1
        )
        if self.request.POST:
            formset = OrderFormSet(
                self.request.POST,
                self.request.FILES,
                instance=self.object
            )
        else:
            queryset = self.object.item_in_order.select_related('product')
            formset = OrderFormSet(instance=self.object, queryset=queryset)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
        context['item_in_order'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        order_items = context['item_in_order']

        with transaction.atomic():
            order = super().form_valid(form)
            if order_items.is_valid():
                order_items.save()

        if self.object.summary_product['total_cost'] == 0.00:
            self.object.delete()

        return order


class DetailOrder(LoginUserOnlyMixin,DetailView):
    model = Order


class DeleteOrder(LoginUserOnlyMixin,DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:index')


def buy_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.STATUS_PAID
    order.save()

    return HttpResponseRedirect(reverse('ordersapp:index'))


@receiver(pre_save, sender=ItemInOrder)
def update_count_item_in_order_save(sender, update_fields, instance, **kwargs):
    if instance.pk:
        instance.product.count += sender.get_item(instance.pk).count - instance.count
    else:
        instance.product.count -= instance.count
    instance.product.save()


@receiver(pre_delete, sender=ItemInOrder)
def update_count_in_order_after_delete(sender, instance, **kwargs):
    instance.product.count += instance.count
    instance.product.save()


@receiver(pre_delete, sender=Order)
def product_quantity_update_delete(sender, instance, **kwargs):
    pass
