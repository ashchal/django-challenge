from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello")

def help(request):
    my_dict ={'insert_me':"hello there how u"}
    return render(request,'appTwo/help.html',context=my_dict)