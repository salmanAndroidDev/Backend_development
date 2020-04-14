from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'home.html')

def translate(request):
    orgin=  request.GET['orginaltext'].lower()
    translation = ''

    for word in orgin.split():
        if word[0] in ['a', 'i', 'e', 'o','u']:
            # vowel
            translation += word
            translation += "yay "
        else:
            # consonant
            translation += word[1:]
            translation += word[0]
            translation += "ay "

    return render(request,'translate.html', {'original': orgin, 'translation':translation})

def about(request):
    return render(request, 'about.html')  



