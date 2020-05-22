from django.db.models.fields.reverse_related import ForeignObjectRel
from django.shortcuts import render, redirect
from .dao_factory import BookingDao, RoomDao


# Create your views here.


def get_one(request, pk):
    ctx = {}
    booking = BookingDao.find_one(pk=pk)
    total_price = BookingDao.get_total_price(booking, booking.order.room.id)
    room = RoomDao.find_one(pk=booking.order.room.id)
    services = RoomDao.get_m2m(room, 'services')
    ctx['booking'] = booking
    ctx['total_price'] = total_price
    ctx['room'] = room
    ctx['room_services'] = services
    ctx['payment'] = total_price - booking.money
    return render(request, 'dao/get_one_booking.html', ctx)


def delete_booking(request, pk):
    booking = BookingDao.find_one(pk=pk)
    BookingDao.delete(booking)
    return redirect('/orm/all_orders/')
