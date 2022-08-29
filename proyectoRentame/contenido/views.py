from django.shortcuts import render, HttpResponse

def principal(request):
    return render(request,"contenido/principal.html")
