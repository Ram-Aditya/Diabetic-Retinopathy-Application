from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import *


def home(request):
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['Main_Img']
            f = form.save(commit=False)
            f.name = name
            f.save()
            FinalValue = evaluate_upload(name)
            if FinalValue < 0 or FinalValue > 4:
                return redirect(error)
            return HttpResponseRedirect(reverse('results', args=(FinalValue,)))
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})


def error(request):
    return render(request, 'error.html')


def about(request):
    return render(request, 'about.html')


def results(request, FinalValue):
    print(FinalValue)
    img_name = "CBMS.png"
    return render(request, 'result.html', {'result': FinalValue, 'img': img_name})


def evaluate_upload(name):
    image = ImageUpload.objects.get(name=name)
    path = "images/" + image.name
    print(path)
    return 3
