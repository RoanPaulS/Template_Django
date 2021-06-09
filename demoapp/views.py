from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    message = "Hi"
    if hour<12:
        message = message+" Good Morning"
    else:
        message = message+" Good Evening"
    name = "Paul"
    dictionary = {'display_dict':date , 'myName':name , 'greetings':message}
    return render(request,'abc.html',context=dictionary)
