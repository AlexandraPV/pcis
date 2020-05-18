# Generated by Django 3.0.6 on 2020-05-17 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back_office', '0002_wish'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('result_price', models.FloatField(default=0)),
                ('booking', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='back_office.Booking')),
            ],
        ),
    ]
