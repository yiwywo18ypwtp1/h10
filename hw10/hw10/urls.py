from django.contrib import admin
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from quotes import views

from quotes.views import RegisterUser, LoginUser

from quotes.forms import CustomPasswordResetForm

from quotes.forms import CustomSetPasswordForm

urlpatterns = [
    path('admin', admin.site.urls),

    path('', views.main_page, name='main_page'),
    path('<str:tag>', views.main_page, name='main_page'),
    path('author/<str:name>', views.author, name='author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),




    path(
        'reset-password/',
        views.ResetPasswordView.as_view(form_class=CustomPasswordResetForm),  # ⬅ Правильно передаем здесь
        name='password_reset'
    ),

    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html', ),
         name='password_reset_done'),


    path(
        'reset-password/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete'),
            form_class=CustomSetPasswordForm  # ⬅ form_class здесь
        ),
        name='password_reset_confirm',
    ),

    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
