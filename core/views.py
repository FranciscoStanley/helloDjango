from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(response, nome, idade):
    return HttpResponse('<h1>Hello, {} de {} anos de idade!</h1>'.format(nome, idade))

def soma(response, num1 = 10, num2 = 20):
    return HttpResponse("<h1>Soma de {} + {} = {}</h1>".format(num1, num2, num1 + num2))