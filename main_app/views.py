from django.shortcuts import render
from django.http import HttpResponse



class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Lolo', 'tabby', 'A very cute cat', 2),  
    Cat('Momo', 'Siamese', 'A very fluffy cat', 3),
    Cat('Kiki', 'Persian', 'A very lazy cat', 5),
    Cat('Neko', 'Bengal', 'A very playful cat', 1),
]

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about (request):
    return render(request, 'about.html')

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})

