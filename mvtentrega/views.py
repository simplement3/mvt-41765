from django.http import HttpResponse
from datetime import datetime

def hola(request):
    return HttpResponse('buenas clase')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'la fecha y hora actual es {fecha_actual}')