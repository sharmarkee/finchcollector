from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm

finches = [
  {'name': 'Ray', 'breed': 'gray', 'color': 'feathery evil', 'age': 6},
  {'name': 'Mark', 'breed': 'brown', 'color': 'docile and sweer', 'age': 7},
]


# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })


def finches_detail(request, finch_id):
 finch = Finch.objects.get(id=finch_id)
 id_list = finch.toys.all().values_list('id')

 toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)

 feeding_form = FeedingForm()
 return render(request, 'finches/detail.html', {
        'finch':finch, 'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
  })
 


class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'color','breed', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'color', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id =finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id = finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id = finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)
