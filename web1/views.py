from web1.models import mails
from web1.forms import SendingEmail
from django.shortcuts import render

# Create your views here.

def homePageLanding(request):

    return render(request, 'web1/base.html')


def home(request):
    
    return render(request, 'web1/home.html')

def Emailing(request):
    if request.method == 'POST':
        fm=SendingEmail(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            num=fm.cleaned_data['c_number']
            msg=fm.cleaned_data['message']
            reg=mails(name=nm,email=em,c_number=num, message=msg)
            reg.save()
            fm=SendingEmail()

    else:
        fm=SendingEmail()
    stud = mails.objects.all()

    return render(request, 'web1/sendingEmail.html',{'form':fm})