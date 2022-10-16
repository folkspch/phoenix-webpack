from django.shortcuts import render

# Create your views here.
def login(request):
    authen_dict = {
        'test' : 'testAuthen'
    }
    return render(request,'authen_app/login.html',context=authen_dict)


def twofa(request):
    twofa_dict = {
        'test' : 'testTwofa'
    }
    return render(request,'authen_app/2fa.html',context=twofa_dict)
