from django.shortcuts import render, get_object_or_404
from .models import Contact, PhoneNumber


def index(request):
    contacts = Contact.objects.select_related().all()
    return render(request, 'index.html', {'contacts': contacts})


def info(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    numbers = PhoneNumber.objects.filter(pk=contact.pk)
    return render(request, 'info.html', {'contact': contact, 'numbers': numbers})