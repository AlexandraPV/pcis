from django.shortcuts import render, redirect
from .containers import Readers, Clients, Configs



def di_month(request):
    ctx = {}
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "kpi.study1@gmail.com",
        "password": "kjj45gl24h%HS",
        "mailbox": "IMAP"
    })

    email_reader = Readers.email_reader()
    ctx['email_reader'] = email_reader
    return render(request, 'di/home.html', ctx)

def di_week(request):
    ctx = {}
    Configs.config.override({
        "domain_name": "smtp.gmail.com",
        "email_address": "kpi.study2@gmail.com",
        "password": "egfv%&h6%^8TFX",
        "mailbox": "SMTP"
    })
    email_reader = Readers.email_reader()
    ctx['email_reader'] = email_reader
    return render(request, 'di/home.html', ctx)

def di_day(request):
    ctx = {}
    Configs.config.override({
        "domain_name": "sandbox.gmail.com",
        "email_address": "kpi.study3@gmail.com",
        "password": "uhDbh44d^*hgwd",
        "mailbox": "SANDBOX"
    })
    email_reader = Readers.email_reader()
    ctx['email_reader'] = email_reader
    return render(request, 'di/home.html', ctx)
