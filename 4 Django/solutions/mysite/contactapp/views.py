from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact
import re

def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        fav_fruit = request.POST['fav_fruit']
        fav_color = request.POST['fav_color']
        contact = Contact(name=name, fav_fruit=fav_fruit, fav_color=fav_color)
        contact.save()

    search_text = request.GET['search_text'] if 'search_text' in request.GET else ''

    output = Contact.objects.filter(name__icontains=search_text) \
                | Contact.objects.filter(fav_fruit__icontains=search_text) \
                | Contact.objects.filter(fav_color__icontains=search_text)

    # contacts = Contact.objects.all()
    # output = []
    # for contact in contacts:
    #     if re.search(search_text, contact.name, re.IGNORECASE) \
    #         or re.search(search_text, contact.fav_fruit, re.IGNORECASE) \
    #         or re.search(search_text, contact.fav_color, re.IGNORECASE):
    #         output.append(contact)

    context = {'contacts': output, 'color':'red'}
    return render(request, 'contactapp/index.html', context)




