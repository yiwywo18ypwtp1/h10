from django.contrib import admin
from django.urls import path

from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
]
