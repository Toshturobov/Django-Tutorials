from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def gaming(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>GAMING</h1>
""") 

def vlogs(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>VLOGS</h1>
""") 
def movies(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>MOVIES</h1>
""") 
def podcast(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>PODCAST</h1>
""") 
def reacts(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>REACTS</h1>
""") 
def xabar(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;gap:20px;}
    </style>

    <h1>XABAR</h1>
""") 

