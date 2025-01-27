from django.shortcuts import render

from quotes.models import Quote
from quotes.models import Writer


def main_page(request):
    all_quotes = Quote.objects.all()
    quotes_list = []

    for i in all_quotes:
        # print(f'{i.writer.name}: - {i.text} | {i.tag}')
        quotes_list.append(i)

    context = {
        'quotes': quotes_list,
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


def login(request):
    return render(request, 'login_page.html')
