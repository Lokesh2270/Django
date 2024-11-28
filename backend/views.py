from django.shortcuts import render
from django.http import JsonResponse,HttpResponse


def sample_get_view(request):
    return HttpResponse("Hello Python",content_type="text/plain")

def sample1(request):
    return JsonResponse({"message":"Hellow formate"})

def lokesh(request):
    return HttpResponse("hello lokesh",content_type="text/plain")