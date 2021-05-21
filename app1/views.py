from django.shortcuts import render
from django.http import HttpResponse
from .forms import user_form
from .models import mymodel


# Create your views here.

def home(request):
    return render(request, 'index.html', {'title': 'First', 'link': 'http://youtube.com'})


# CRUD operations

# CREATE operation
def create(request):
    form = user_form()
    if request.method == 'POST':
        form = user_form(request.POST)
        form.save()

    return render(request, 'form.html', {'form': form})


# Read operation
def read(request):
    s = mymodel.objects.all()
    return render(request, 'read.html', {'s': s})


# UPDATE operation
def update(request, id):
    ud = mymodel.objects.get(id=id)
    form = user_form(instance=ud)
    print("id_detail : ",  id)

    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated successfully')
    return render(request, 'form.html', {'form': form})


# Delete operation

def DeleTe(request, id):
    dlt = mymodel.objects.get(pk=id)
    dlt.delete()

    return HttpResponse('<h1>Data deleted Successfully</h1>')
