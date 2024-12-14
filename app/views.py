from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render (request , "base.html")

def home(request):
    return render(request , 'home.html')

def result_view(request):
    name = request.GET.get('name', 'Unknown')
    image = request.GET.get('image', 'default.jpg')
    score = request.GET.get('score', '0')

    context = {
        'name': name,
        'image': image,
        'score': score,
    }
    return render(request, 'result.html', context)