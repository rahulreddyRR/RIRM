from django.shortcuts import render
from account.forms import customerform
from account.models import customerinfo
# Create your views here.

def index(request):
    data_saved = False
    if request.method == "POST":
        customer_info = customerform(data=request.POST)
        if customer_info.is_valid:
            customer_info.save()
            data_saved = True
        else:
            print(customer_info.errors)
    else:
        customer_form=customerform()
    return render(request,'index.html',{'customerform':customerform,'data_saved':data_saved})

def details(request):
    if request.method =='POST':
        name = request.POST.get('Full_Name')
        user_namedata = customerinfo.objects.filter(FullName=name)
        return render(request,'details.html',{'data':user_namedata})
    return render(request,'details.html')
