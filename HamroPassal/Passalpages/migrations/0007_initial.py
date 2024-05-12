# Generated by Django 5.0.4 on 2024-04-29 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Passalpages', '0006_remove_itemsincart_cart_info_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('ratting', models.IntegerField()),
                ('amount', models.FloatField()),
                ('sale', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='carts_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_items', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckOutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phonenum', models.IntegerField(blank=True, null=True)),
                ('shipemail', models.EmailField(max_length=254)),
                ('Order_Notes', models.CharField(blank=True, max_length=350, null=True)),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('Street_Name', models.CharField(max_length=50)),
                ('Full_Address', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='itemsInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Passalpages.carts_info')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Passalpages.product')),
            ],
        ),
        migrations.CreateModel(
            name='shipping_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_number', models.CharField(max_length=100)),
                ('ordered_Date', models.DateField(auto_now_add=True)),
                ('deliver_Date_on', models.DateField(null=True)),
                ('recived_items', models.BooleanField(default=False)),
                ('paid_money', models.BooleanField(default=False)),
                ('checkout_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Passalpages.checkoutinfo')),
            ],
        ),
        migrations.CreateModel(
            name='checkout_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Passalpages.product')),
                ('shippinginfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Passalpages.shipping_info')),
            ],
        ),
    ]