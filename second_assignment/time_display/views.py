from django.shortcuts import render, HttpResponse,redirect
from time import strftime

# from django.http import JsonResponse
    
def index(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M:%p")
    }
    return render(request,'index.html', context)

def index2(request):
    return redirect("/")
