# Generated by Django 5.0.4 on 2024-04-29 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Passalpages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemsincart',
            old_name='carts_info',
            new_name='cart_info',
        ),
    ]
