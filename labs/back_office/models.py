from django.db import models


# Create your models here.

class Service(models.Model):
    price = models.FloatField(verbose_name='Цена услуги')
    name = models.CharField(max_length=255, verbose_name='Название услуги', blank=True, null=True)
    text = models.TextField(default='', verbose_name='Описание услуги')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название номера', blank=True, null=True)
    count_seats = models.IntegerField(default=2, verbose_name='Кол-во мест', blank=True, null=True)
    description = models.TextField(max_length=255, default='', verbose_name='Описание', blank=True, null=True)
    view_from_window = models.CharField(max_length=255, default='', verbose_name='Вид из окна', blank=True, null=True)
    services = models.ManyToManyField(Service, verbose_name='Услуги')
    rate = models.IntegerField(default=5, blank=True, null=True)
    price = models.FloatField(verbose_name='Цена номера')

    def __str__(self):
        return self.name


class Client(models.Model):
    STATUS = (
        ('base', 'Обычный'),
        ('vip', 'VIP'),
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    email = models.CharField(verbose_name='Телефон', blank=True, null=True, max_length=16)
    status = models.CharField(choices=STATUS, default='base', max_length=20)
    date_birth = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return '{name} {surname} статус - {status}'.format(name=self.first_name, surname=self.second_name,
                                                           status=self.status)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    date_from = models.DateField(verbose_name='Дата заезда')
    date_to = models.DateField(verbose_name='Дата выезда')
    optional_services = models.ManyToManyField(Service, blank=True, null=True)
    total_price = models.FloatField(default=0, blank=True, null=True)

    def get_services(self):
        return self.optional_services.all()

    def get_booking(self):
        try:
            return Booking.objects.get(order=self)
        except Exception as e:
            print(type(e), e)

    def __str__(self):
        return '{} {}'.format(self.client, str(self.date_from) + ' ' + str(self.date_to))


class Booking(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, default='', null=True, blank=True)
    passport = models.CharField(max_length=255, verbose_name='Паспортные данные', default='', null=True, blank=True)
    money = models.FloatField(verbose_name='Сколько денег оставили перед вьездом')

    def __str__(self):
        return 'Заказ {}'.format(self.order)


class Job(models.Model):
    TYPE = (
        ('cleaner', 'Служба уборки'),
        ('parking', 'Парковка'),
        ('reception', 'Рецепция'),
        ('cooker', 'Ресторан'),
        ('tour_guide', 'Экскурсовод')
    )
    type = models.CharField(max_length=255, choices=TYPE)
    occupation = models.CharField(max_length=255, verbose_name='Должность')


class Personal(models.Model):
    SEX = (
        ('male', "Мужской"),
        ('female', "Женский")
    )
    TYPE = (
        ('back', 'BACK'),
        ('front', 'FRONT'),
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    second_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)
    date_birth = models.DateField(verbose_name='Дата рождения')
    sex = models.CharField(max_length=255, choices=SEX, default='female', verbose_name='Пол')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    salary = models.FloatField(verbose_name='ЗП')
    type = models.CharField(max_length=255, verbose_name='Back или Front Office', choices=TYPE)


class Wish(models.Model):
    date_now = models.DateTimeField(auto_now_add=True)
    date_when = models.DateTimeField(verbose_name='На когда это сделать')
    date_done = models.DateTimeField(verbose_name='Когда сделано')
    who = models.ForeignKey(Personal, on_delete=models.SET_NULL, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    room = models.ForeignKey(Booking, on_delete=models.SET_NULL, blank=True, null=True)
    msg = models.TextField(default='', max_length=2555, blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='Статус заявки')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)


class FinishBooking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField(max_length=1000)
    result_price = models.FloatField(default=0)
