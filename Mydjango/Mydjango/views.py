from django.shortcuts import render
from django.http import HttpResponse , JsonResponse



def home(request):
    try:
        return render(request , "index.html")
    except Exception as e:
        return  JsonResponse({
            'success' : False,
            "error" : repr(e)
        })