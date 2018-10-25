from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Contact, PhoneNumber
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.select_related().all()
    return render(request, 'index.html', {'contacts': contacts})


def info(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    numbers = PhoneNumber.objects.filter(contact=contact)
    return render(request, 'info.html', {'contact': contact, 'numbers': numbers})


def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            contact.save()
            messages.info(request, 'Contact has been added successfully')
            return redirect('/')
    return render(request, 'add.html', {'form': form})