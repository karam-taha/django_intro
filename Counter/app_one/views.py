from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse,redirect

def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    request.session['count']+=1
    return render (request,"index.html")

def destroy_session(request):
    del request.session['count']
    return redirect ("/")

def add_session(request):
    if 'count' not in request.session:
        request.session['count']=0
    request.session['count']+=1
    return redirect ("/")