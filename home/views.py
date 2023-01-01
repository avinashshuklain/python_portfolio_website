from datetime import date
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable' : 'This is sent!'
    }
    # return HttpResponse('This is home page.')
    return render(request, 'index.html',context)

def about(request):
    # return HttpResponse('This is about page.')
    return render(request, 'about.html')

def services(request):
    # return HttpResponse('This is services page.')
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse('This is contact page.')
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        contact = Contact(name=name,email=email,address1=address1,address2=address2,city=city,phone=phone,date=date.today())
        contact.save()
        messages.success(request, 'Details has been submitted successfully!')
    return render(request, 'contact.html')

