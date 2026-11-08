from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def home(request):
    # return HttpResponse("<h1>Hello This is my First Response on Page</h1>")

    people = [
        {'name': "Vishwam Solanki", 'age': 23},
        {'name': "Rahul singh", 'age': 15},
        {'name': "Ujwall Goyal", 'age': 31},
        {'name': "Ruchi solanki", 'age': 10},
        {'name': "Raj singh", 'age': 58},
        {'name': "Ram kapoor", 'age': 96},
    ]

    return render(request, 'index.html', context={'people': people})


def secondary_page(request):

    return HttpResponse('''
        <h2>This is the Secondary page</h2>
        <p>hello I am the success Page</p>
    ''')


def aboutus(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    pass


def register(request):
    pass