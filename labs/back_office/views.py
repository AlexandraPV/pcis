from django.shortcuts import render, redirect
from .models import Client
# Create your views here.
from django.db import connection
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


def home(request):
    ctx = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')
        status = request.POST.get('status')
        date_birth = request.POST.get('date_birth')
        # ORM
        Client.objects.create(
            first_name=first_name,
            second_name=second_name,
            middle_name=middle_name,
            email=email,
            status=status,
            date_birth=date_birth,
        )

        # SQL QUERY
#         cursor = connection.cursor()
#         cursor.execute("""
#         INSERT INTO `back_office_client`
#             (`first_name`, `second_name`, `middle_name`, `email`, `status`, `date_birth`)
#         VALUES ('{first_name}', '{second_name}', '{middle_name}', '{email}', '{status}', '{date_birth}')
# """.format(first_name=first_name, second_name=second_name,
#            middle_name=middle_name, email=email,
#            status=status, date_birth=date_birth))
#         cursor.close()
        return redirect('home:client_list')
    return render(request, 'home.html', ctx)


def client_list(request):
    ctx = {}
    #ORM
    clients = Client.objects.all()
    ctx['clients'] = clients
    #


    # SQL QUERY
    # cursor = connection.cursor()
    # cursor.execute("""
    # SELECT `back_office_client`.`id`, `back_office_client`.`first_name`,
    #  `back_office_client`.`second_name`,
    #   `back_office_client`.`middle_name`,
    #   `back_office_client`.`email`,
    #  `back_office_client`.`status`,
    #   `back_office_client`.`date_birth`
    #   FROM `back_office_client`
    #
    # """)
    # ctx['clients'] = cursor.fetchall()
    # cursor.close()
    return render(request, 'list.html', ctx)


def update(request, pk):
    ctx = {}

    # ORM
    client  = Client.objects.get(id=pk)
    ctx['client'] = client

    # SQL QUERY
    # cursor = connection.cursor()
    # cursor.execute("""
    #    SELECT `back_office_client`.`id`, `back_office_client`.`first_name`,
    #     `back_office_client`.`second_name`,
    #      `back_office_client`.`middle_name`,
    #      `back_office_client`.`email`,
    #     `back_office_client`.`status`,
    #      `back_office_client`.`date_birth`
    #      FROM `back_office_client`
    #     WHERE id = {}
    #    """.format(pk))
    # ctx['client'] = cursor.fetchone()
    # ctx['id'] = pk
    # cursor.close()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')
        status = request.POST.get('status')
        date_birth = request.POST.get('date_birth')

        #ORM
        Client.objects.update_or_create(
            first_name=first_name,
            second_name=second_name,
            middle_name=middle_name,
            email=email,
            status=status,
            date_birth=date_birth,
            fields = {
                'id': pk
            }
        )

        # SQL QUERY
        # cursor = connection.cursor()
        # cursor.execute(
        #     """
        #     UPDATE back_office_client
        #     SET
        #         first_name = '{first_name}',
        #         second_name = '{second_name}',
        #         middle_name = '{middle_name}',
        #         email = '{email}',
        #         status = '{status}',
        #         date_birth = '{date_birth}'
        #     WHERE
        #         id = {id_};
        # """.format(
        #         first_name=first_name,
        #         second_name=second_name,
        #         middle_name=middle_name,
        #         email=email,
        #         status=status,
        #         date_birth=date_birth,
        #         id_=pk
        #     ))
        # cursor.close()
        return redirect('home:client_list')
    return render(request, 'update.html', ctx)


def delete(request, pk):
    #ORM
    Client.objects.get(id=pk).delete()

    # cursor = connection.cursor()
    # cursor.execute(
    #     """
    #       DELETE FROM back_office_client
    #       WHERE id={};
    #       """.format(pk)
    # )
    # cursor.close()
    return redirect('home:client_list')
