import requests
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  response = requests.get('https://catfact.ninja/fact')
  return render(request, 'about.html', {
    'fact': response.json().get('fact')
  })

def cat_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # Obtain list of toys ids that the cat has
  toys_cat_has = cat.toys.all().values_list('id')
  # Query for toys that the cat doesn't have
  toys = Toy.objects.exclude(id__in=toys_cat_has)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    'cat': cat,
    'toys': toys,
    'feeding_form': feeding_form
  })

class CatCreate(CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']
  # success_url = '/cats/{id}'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

def add_feeding(request, cat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('cat-detail', cat_id=cat_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyDetail(DetailView):
  model = Toy

class ToyList(ListView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def associate_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id__exact=cat_id)
  cat.toys.add(toy_id)
  return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
    cat = Cat.objects.get(id__exact=cat_id)
    cat.toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat_id)