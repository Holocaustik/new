from django.shortcuts import render

from .models import Portfolio


def home(request):
    project = Portfolio.objects.all()
    return render(request, 'portfolio/home.html', {'project': project})
