from select import select
from telnetlib import STATUS
from django.shortcuts import render
from .serializers import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import *

# Create your views here.
@csrf_exempt
def getdata(request):
    if request.method == "GET":
        selectdata = Patient.objects.all()
        serializer = Detailapi(selectdata,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == "POST":
        data=JSONParser().parse(request)
        serializer = Detailapi(data= data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


@csrf_exempt
def modify(request,id):
    if request.method == 'GET':
        selectdata = Patient.objects.get(id=id)
        serializer = Detailapi(selectdata)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        selectdata = Patient.objects.get(id=id)
        data = JSONParser().parse(request)
        serializer = Detailapi(selectdata,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.erros,status=400)

    elif request.method == 'DELETE':
        selectone = Patient.objects.get(id=id)
        selectone.delete()
        return HttpResponse(status=201)


@csrf_exempt
def getdatadoctor(request):
    if request.method == "GET":
        selectdata = Doctor.objects.all()
        serializer = Detailapi(selectdata,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == "POST":
        data=JSONParser().parse(request)
        serializer = Detailapi(data= data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


@csrf_exempt
def modifydoctor(request,id):
    if request.method == 'GET':
        selectdata = Doctor.objects.get(id=id)
        serializer = Detailapi(selectdata)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        selectdata = Doctor.objects.get(id=id)
        data = JSONParser().parse(request)
        serializer = Detailapi(selectdata,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.erros,status=400)

    elif request.method == 'DELETE':
        selectone = Doctor.objects.get(id=id)
        selectone.delete()
        return HttpResponse(status=201)
