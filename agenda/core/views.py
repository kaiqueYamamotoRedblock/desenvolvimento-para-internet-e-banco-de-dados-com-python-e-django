from django.shortcuts import render
from core.models import Evento

# Create your views here.
def list_events(request):
    evento = Evento.objects.all()
    dados = { 'eventos': evento}
    return render(request, 'agenda.html', dados)
