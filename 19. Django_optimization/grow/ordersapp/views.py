from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from ordersapp.forms import OrderForm, OrderItemForm
from ordersapp.models import Order, ItemInOrder


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrder(CreateView):
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

        if self.object.total_cost == 0:
            self.object.delete()

        return order


class UpdateOrder(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:index')

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
            formset = OrderFormSet(instance=self.object)
        context['item_in_order'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['item_in_order']

        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.save()

        if self.object.total_cost == 0:
            self.object.delete()

        return order


def buy_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.STATUS_PAID
    order.save()

    return HttpResponseRedirect(reverse('ordersapp:index'))
