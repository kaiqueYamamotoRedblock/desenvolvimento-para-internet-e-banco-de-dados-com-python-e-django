from django.shortcuts import render, HttpResponse


# Create your views here.
def sum(request, value_1, value_2):
    sum = value_1 + value_2
    return HttpResponse('O valor é: {}'.format(sum))


def multiplicacao(request, value_1, value_2):
    cont = value_1 * value_2
    return HttpResponse('O valor é: {}'.format(cont))


def subtracao(request, value_1, value_2):
    cont = value_1 - value_2
    return HttpResponse('O valor é: {}'.format(cont))


def divisao(request, value_1, value_2):
    cont = value_1 / value_2
    return HttpResponse('O valor é: {}'.format(cont))
