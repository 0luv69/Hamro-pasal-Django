from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(carts_info)
admin.site.register(itemsInCart)
admin.site.register(CheckOutInfo)
admin.site.register(checkout_products)
admin.site.register(shipping_info)

