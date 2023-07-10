from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:red;}
    </style>

    <h1>Home</h1>
""") 

def about(request):
    return HttpResponse("""
    <style>
        h1{color:blue;}
        body{display:flex;justify-content:center;background-color:yellow;}
    </style>

    <h1>About</h1>
""") 
