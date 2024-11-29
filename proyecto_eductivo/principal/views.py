from django.shortcuts import render, get_object_or_404
from .models import Estudiante

# Create your views here.
def home(request):
    estudiantes = Estudiante.objects.all()
    print(type(estudiantes))
    return render(request, 'principal/home.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request, 'principal/detalle.html', {'estudiante': estudiante})