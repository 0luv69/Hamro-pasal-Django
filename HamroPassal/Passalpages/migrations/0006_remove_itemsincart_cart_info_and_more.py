# Generated by Django 5.0.4 on 2024-04-29 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Passalpages', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsincart',
            name='cart_info',
        ),
        migrations.RemoveField(
            model_name='checkout_products',
            name='product',
        ),
        migrations.RemoveField(
            model_name='checkout_products',
            name='shippinginfo',
        ),
        migrations.RemoveField(
            model_name='checkoutinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shipping_info',
            name='checkout_info',
        ),
        migrations.RemoveField(
            model_name='itemsincart',
            name='product',
        ),
        migrations.DeleteModel(
            name='carts_info',
        ),
        migrations.DeleteModel(
            name='checkout_products',
        ),
        migrations.DeleteModel(
            name='CheckOutInfo',
        ),
        migrations.DeleteModel(
            name='shipping_info',
        ),
        migrations.DeleteModel(
            name='itemsInCart',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]