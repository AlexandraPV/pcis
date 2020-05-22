from .dao import BaseDao
from back_office.models import Booking, Room, Service, Order


class OrderDao(BaseDao):
    MODEL_NAME = Order


class ServiceDao(BaseDao):
    MODEL_NAME = Service


class RoomDao(BaseDao):
    MODEL_NAME = Room



class BookingDao(BaseDao):
    MODEL_NAME = Booking

    @classmethod
    def get_total_price(cls, booking, room_id):
        room = RoomDao.find_one(room_id)
        order = OrderDao.find_one(booking.order.id)
        services = OrderDao.get_m2m(obj=order, field_name='optional_services')
        return sum([service.price for service in services]) + room.price
