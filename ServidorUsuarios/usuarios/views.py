import json
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from .logic.logic_u import get_paciente
from .models import Paciente


# Create your views here.

def crear_paciente(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if get_paciente(data_json)==None:
            paciente = Paciente()
            paciente.nombre = data_json['nombre']
            paciente.celular = data_json['celular']
            paciente.correo = data_json['correo']
            paciente.cedula = data_json['cedula']
            paciente.save()
            return HttpResponse("successfully created measurement")
        else:
            return HttpResponse("unsuccessfully created measurement. Variable or place does not exist")


@api_view(['GET'])
def data_view(request):
    return Response({"message": "Datos desde Microservicio B"})
