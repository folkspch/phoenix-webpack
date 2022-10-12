from django.shortcuts import render
from phoenix.user_app.models import Staff

# Create your views here.
def user(request):
    staff_list = Staff.objects.order_by('first_name')
    user_dict = {
        'test' : 'testUser'
    }
    return render(request,'user_app/user.html',context=user_dict)
