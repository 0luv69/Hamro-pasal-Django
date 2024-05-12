"""
URL configuration for HamroPassal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Passalpages.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', home_pg, name='home'),
    path('short/<short_id>', short_request, name='short_request'),
    path('cart', cart_pg, name='cart'),
    path('addcart/<id>', add_cart, name='addcart'),
    path('rmvcart/<id>', rmv_cart, name='rmvcart'),
    path('checkout/', checkout_pg, name='checkout'),
    path('get_data', get_data, name='get_data'),
    path('producthistory/', producthistory_pg, name='producthistory'),



    path('login', login_pg, name='login'),
    path('logout', logout_pg, name='logout'),
    path('signup', signup_pg, name='signup'),


    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)