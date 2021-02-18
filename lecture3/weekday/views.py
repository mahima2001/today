from django.http import HttpResponse
from django.shortcuts import render
import datetime
dr={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
# Create your views here.
def index(request):
    now= datetime.datetime.today()
    return render(request,"weekday/index.html",{
        "date":str(now.day)+"-"+str(now.month)+"-"+str(now.year),
        "weekday":dr[now.weekday()].upper(),
        "newyr":now.month==1 and now.day==1})

#def mahima(request):
    #return HttpResponse("Hello,world!")


    