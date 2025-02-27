from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView

from quotes.models import Quote, Writer, Tag

from quotes.forms import RegistrationForm, LoginForm, AddQuoteForm

from quotes.forms import CustomPasswordResetForm


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

    # print(tags_list)

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
            break

    context = {
        'author_name': name,
        'writer': writer
    }
    return render(request, 'author_page.html', context=context)


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuoteForm(request.POST)
        if form.is_valid():
            quote_text = form.cleaned_data['text']
            author_name = form.cleaned_data['writer']
            tag_name = form.cleaned_data['tag']

            writer, _ = Writer.objects.get_or_create(name=author_name)
            tag, _ = Tag.objects.get_or_create(tag_name=tag_name)

            Quote.objects.create(text=quote_text, writer=writer, tag=tag)

            return redirect('main_page')
    else:
        form = AddQuoteForm()

    context = {
        'form': form,
    }

    return render(request, 'add_quote_page.html', context=context)


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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    html_email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'password_reset_subject.txt'
    form_class = CustomPasswordResetForm
