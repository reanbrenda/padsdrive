import email
from email import message
from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request,"index.html",{})

def contact(request):
    
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        
        send_mail(
            "message from"+name,
             message,
             name,
             email,
            ["mukindia67@gmail.com"]
            
        )
        return render(request,"contact.html",{"name":name})
    else:
        return render(request,"contact.html")
