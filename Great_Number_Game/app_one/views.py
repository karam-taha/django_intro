from django.shortcuts import render,HttpResponse,redirect
import random 

def root(request):
    if 'random' not in request.session:
        request.session['random'] = random.randint(1, 100)
        request.session['status'] = 'new'
        request.session['guesses'] = 0
        print('Status is:', request.session['status'])
        print('Random Number is', request.session['random'])
    return render(request,"index.html")

def guess(request):
    if request.method == "POST":
        if request.POST['guess-value']:
            if int(request.POST['guess-value']) > request.session['random']:
                request.session['status'] = 'high'
                request.session['guesses'] += 1
            elif int(request.POST['guess-value']) < request.session['random']:
                request.session['status'] = 'low'
                request.session['guesses'] += 1
            else:
                request.session['status'] = 'win'
                request.session['guesses'] += 1
            if request.session['status'] != 'win' and request.session['guesses'] >= 5:
                request.session['status'] = 'lose'
    return redirect("/")

def destroy(request):
    del request.session['random']
    return redirect("/")