from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import staticfiles

from .load_index import preface

import os, sys

# Index of books
def index(request):
    
    a = {
        'preface':preface()
    }
    return render(request, 'booklist/index.html', a)

# Details for each books
def book(request, book_id):
    return HttpResponse("This is book %d" % book_id)


