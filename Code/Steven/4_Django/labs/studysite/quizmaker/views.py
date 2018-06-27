from django.shortcuts import render
from django.http import HttpResponse

import csv


def index(request):
    return render(request, 'howdy')


def import_text(request):

    with open('inputfile.txt', newline='') as inputfile:
        results = list(csv.reader(inputfile))

    print(inputfile)
    print(results)

    return render(request, 'howdy')
