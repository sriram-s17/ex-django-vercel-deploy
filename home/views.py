from django.shortcuts import render
from .forms import *

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def add_data_page(request):
    context = {
        'form': SampleModelForm
    }
    if request.method == 'POST':
        form_data = SampleModelForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
    return render(request, 'add_data.html', context)

def view_data_page(request):
    context = {
        "data": SampleModel.objects.all()
    }
    return render(request, 'view_data.html', context)