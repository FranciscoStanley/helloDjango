from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(response, nome, idade):
    return HttpResponse('<h1>Hello, {} de {} anos de idade!</h1>'.format(nome, idade))
