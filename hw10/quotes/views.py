from django.shortcuts import render

from quotes.models import Quote


def main_page(request):
    all_quotes = Quote.objects.all()
    quotes_list = []

    for i in all_quotes:
        print(f'{i.writer.name}: {i.title} - {i.text}')
        quotes_list.append(i)

    context = quotes_list
    return render(request, 'index.html', context={'quotes': all_quotes})
