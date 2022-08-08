"""Irrigation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import trassir.views
import valley.views

admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'Администрирование систем полива и видеонаблюдения'

urlpatterns = [
    path('admin/', admin.site.urls),
### Video Servers
    path('videosrv_list/', trassir.views.videosrv_list, name='videosrv_list'),
    path('videosrv_list/<int:pk>', trassir.views.cameras_detail, name='videosrv_list'),
    path('videosrv_create/', trassir.views.videosrv_create, name='videosrv_create'),
    path('videosrv_update/<int:pk>', trassir.views.videosrv_update, name='videosrv_update'),
### Cameras
    path('cameras_list', trassir.views.cameras_list, name='cameras_list'),
    path('cameras_list/<int:pk>', trassir.views.cameras_detail, name='cameras_list'),
### Systems
    path('systems_list', valley.views.systems_list, name='systems_list'),
    path('states_list', valley.views.states_list, name='states_list'),
]