from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random

def index(request):
    # template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date' : now
    } # index.html에 동적으로 view method에서 정의한 변수들을 삽입하기 위한 object
    # -> for templating
    # return HttpResponse(template.render(context, request)) # for rendering
    return render(request, 'first/index.html', context)

# Create your views here.
def select(request):
    context = {}
    return render(request, 'first/select.html', context)



def result(request):
    chosen = int(request.GET['number'])

    result = []
    if chosen >= 1 and chosen <= 45:
        result.append(chosen)

    box = []
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(result) < 6:
        result.append(box.pop())

    context = {
        'numbers' : result
    }
    return render(request, 'first/result.html', context)
