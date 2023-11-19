from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('Hello World')


def hello_params(request, nome):
    return HttpResponse('Hello, {}'.format(nome))
