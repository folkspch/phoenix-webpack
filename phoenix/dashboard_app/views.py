from django.shortcuts import render

# Create your views here.
def dashboard(request):
    dashboard_dict = {
        'test' : 'testDashboard'
    }
    return render(request,'dashboard_app/dashboard.html',context=dashboard_dict)
