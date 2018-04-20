from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import staticfiles

# Index of books
def index(request):
    return render(request, 'booklist/index.html', {'title':u'snowyjone 和他心爱的书们'})

# Details for each books
def book(request, book_id):
    return HttpResponse("This is book %d" % book_id)


