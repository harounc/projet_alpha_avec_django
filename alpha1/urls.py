"""
URL configuration for alpha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import index, users, users_details, users_devices
from django.contrib import admin
from django.urls import path

from .views import index, users, users_details, users_devices

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<str:route>/', index),
    path('users/', users),
    path('users/<int:id_user>', users_details),
    path('users/<int:id_user>/devices/<int:id_device>', users_devices),
]