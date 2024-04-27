from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

# Create your views here.
def index(request):
    if  request.method=='POST':
        session_id=request.POST.get('sessionId')
        service_code=request.POST.get('serviceCode')
        phone_number=request.POST.get('phoneNumber')
        text=request.POST.get('text')
        response=""

        if text=="":
            response=" Welcome to our news updates \n"
            response+="1. sport \n"
            response +="2. politics \n"
            response += "3. Local \n"
        
        elif text =="1":
            response ="please select news program you wish\n"
            response +="1. Daily \n"
            response += "2. weekly \n"
            response +="3. monthly \n"

        elif text == "1*1":
            pass

        elif text=="1*2":
            pass
        elif text =="1*3":
            pass
        elif text =="1*1*1":
            pass
        elif text =="1*2*1":
            pass
        elif text =="1*3*!":
            pass
        elif text =="1*1*2":
            pass
        elif text =="1*2*2":
            pass
        elif text =="1*3*2.":
            pass
        else:
            response="please insert the correct answer"