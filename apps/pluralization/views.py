from django.shortcuts import render
import inflect
import sys

def index(request):
    word = request.POST.get('word')
    if word:
        p = inflect.engine()
        word = p.plural(word)


    return render(request, 'pluralization/index.html', {
        'word': word
    })
