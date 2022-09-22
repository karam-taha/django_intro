from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime
import random

def root(request):
    return render (request,"index.html")

def process_money(request):
    now=strftime("%B %d %Y %I:%M:%p")
    
    if request.method == 'POST':
        activities = []
        if 'gold' not in request.session:
            request.session['gold'] = 0

        if request.POST['click'] == 'farm':
            random_number = random.randint(10, 20)
            request.session['gold'] += random_number
            activities.append(f'You entered a farm and earned {random_number} gold. ({now})')

        if request.POST['click'] == 'cave':
            random_number = random.randint(10, 20)
            request.session['gold'] += random_number
            activities.append(f'You entered a cave and earned {random_number} gold. ({now})')

        if request.POST['click'] == 'house':
            random_number = random.randint(10, 20)
            request.session['gold'] += random_number
            activities.append(f'You entered a house and earned {random_number} gold. ({now})')

        if request.POST['click'] == 'quest':
            random_number = random.randint(-50,50)
            request.session['gold'] += random_number
            if random_number < 0:
                activities.append(f'You failed a quest and lost {random_number*-1} gold. Ouch! ({now})')
            else:
                activities.append(f'You Completed a quest and earned {random_number} gold. ({now})')

        if 'activities' not in request.session:
            request.session['activities'] = []
        else:
            request.session['activities'] += activities
        # del request.session['activities']
        # del request.session['gold']
    return redirect ("/")

    