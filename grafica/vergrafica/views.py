from django.shortcuts import render
from . models import Alumno


# Create your views here.
def chart_view(request):
    data = Alumno.objects.all()
    return render(request, 'vergrafica\chart.html', {'data': data})