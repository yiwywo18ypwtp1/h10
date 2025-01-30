from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from quotes.models import Quote, Writer, Tag

from quotes.forms import RegistrationForm, LoginForm


def main_page(request, tag=None):
    if tag:
        all_quotes = Quote.objects.filter(tag__tag_name__icontains=tag)
    else:
        all_quotes = Quote.objects.all()

    quotes_list = []
    for i in all_quotes:
        quotes_list.append(i)

    all_tags = Tag.objects.all()
    tags_list = []
    for i in all_tags:
        tags_list.append(i)

    print(tags_list)

    context = {
        'quotes': quotes_list,
        'all_tags': tags_list,
        'tag': tag,
    }
    return render(request, 'index_page.html', context=context)


def author(request, name):
    all_writers = Writer.objects.all()
    writer = ''
    for i in all_writers:
        if i.name == name:
            writer = i
            # print(f'writer = {writer}')
            break

    context = {
        'author_name': name,
        'writer': writer
    }
    return render(request, 'author_page.html', context=context)


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('main_page')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login_page.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    return redirect('login')
