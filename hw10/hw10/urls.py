from django.contrib import admin
from django.urls import path

from quotes import views

from quotes.views import RegisterUser, LoginUser

urlpatterns = [
    path('admin', admin.site.urls),

    path('', views.main_page, name='main_page'),
    path('<str:tag>', views.main_page, name='main_page'),
    path('author/<str:name>', views.author, name='author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
