from django.shortcuts import render


def index(request):
    return render(request, 'user/index.html')


def home(request):
    return render(request, 'user/u_dash.html')
