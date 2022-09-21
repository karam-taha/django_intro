from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return render (request,"index.html")

def result(request):
    if request.method == "POST":
        request.session['name']=request.POST['name']
        request.session['location']=request.POST['location']
        request.session['language']=request.POST['language']
        request.session['comment']=request.POST['comment']
        return redirect ("result")

def show(request):
    return render (request,"result.html")
