from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contactapp/index.html', context)

