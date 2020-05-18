from django.shortcuts import render, redirect
from django import forms
from back_office.models import Order, Client, Booking


# Create your views here.

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['total_price']


def create_order(request):
    ctx = {}
    ctx['form'] = OrderForm()
    if request.method == 'POST':
        client_id = request.POST.get('client')
        room_id = request.POST.get('room')
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        optional_services = request.POST.getlist('optional_services')
        new_order = Order(
            client_id=client_id,  # one-to-many relation (FK)
            room_id=room_id,  # one-to-many relation (FK)
            date_from=date_from,
            date_to=date_to,
        )
        new_order.save()
        for service_id in optional_services:
            new_order.optional_services.add(int(service_id))  # add id_service (many_to_many relation)
        new_order.save()
    return render(request, 'orm/create_order.html', ctx)


def all_orders(request):
    ctx = {}
    ctx['orders'] = Order.objects.all()
    return render(request, 'orm/all_orders.html', ctx)


def delete_order(request, pk):
    try:
        Order.objects.get(id=pk).delete()
    except Exception as e:
        print(type(e), e)
    return redirect('orm:all_orders')


def update_order(request, pk):
    ctx = {}
    order = Order.objects.get(id=pk)
    ctx['form'] = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid!!')
    return render(request, 'orm/create_order.html', ctx)


def approve(request, pk):
    ctx = {}
    order = Order.objects.get(pk=pk)
    ctx['order'] = order
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        passport = request.POST.get('passport')
        money = request.POST.get('money')
        Booking.objects.create(order_id=order_id, passport=passport, money=money)
        return redirect('orm:all_orders')
    return render(request, 'orm/create_booking.html', ctx)


def update_approve(request, pk):
    ctx = {}
    booking = Booking.objects.get(pk=pk)
    ctx['booking'] = booking
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        passport = request.POST.get('passport')
        money = request.POST.get('money')
        Booking.objects.update_or_create(id=pk, defaults=dict(passport=passport, money=money))
        return redirect('orm:all_orders')
    return render(request, 'orm/update_booking.html', ctx)
