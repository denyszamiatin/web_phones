from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.select_related().all()
    return render(request, 'index.html', {'contacts': contacts})


def info(request, c_id):
    print(c_id)
    return render(request, 'info.html')