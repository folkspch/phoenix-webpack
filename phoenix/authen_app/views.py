from django.shortcuts import render

# Create your views here.
def authen(request):
    authen_dict = {
        'test' : 'testAuthen'
    }
    return render(request,'authen_app/authen.html',context=authen_dict)
