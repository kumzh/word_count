from django.shortcuts import render     #render传达一个网页给用户
from django.http import HttpResponse


# Create your views here.
def index_1(request):
    return HttpResponse('<h1>index</h1>')

def home(request):
    return render(request,"home.html")

def count(request):
    txt = request.GET["text"]
    total_count = len(txt)
    dit = {}
    for w in txt:
        if w not in dit:
            dit[w] = 1
        else:
            dit[w] += 1
    sort = sorted(dit.items(),key=lambda m:m[1],reverse=True)
    return render(request,"count.html",{"count":total_count,
                                        "txt":txt,
                                        "sortcount":sort})

def about(request):
    return render(request,"about.html")