from django.shortcuts import render

# Create your views here.
def loan(request):
    loan_dict = {
        'test' : 'testLoan'
    }
    return render(request,'loan_app/loan.html',context=loan_dict)