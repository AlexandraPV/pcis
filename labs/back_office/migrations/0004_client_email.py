# Generated by Django 3.0.6 on 2020-05-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0003_finishbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Телефон'),
        ),
    ]
