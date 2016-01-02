from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def clinic(request):
    return render(request, 'clinic.html', {})


def doctor(request):
    return render(request, 'doctor.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    return render(request, 'contact.html', {})
