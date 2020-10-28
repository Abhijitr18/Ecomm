from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import customerform, orderform
from .models import Customer1,Orders
def view1 (req):
    request = req
    template_name = 'firstapp/home.html'
    context = {}
    return render(request, template_name, context)

def addCustomer(request):
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['city']
        p = request.POST['phone']
        cust = Customer1(name=n,city=c,phone=p)
        cust.save()
        return HttpResponse(f'New Customer Added')
    elif request.method=='GET':
        print('Get req recived')
        return render(request,'firstapp/all_cust.html')

def all_customer(request):
    all_cust = Customer1.objects.all()
    template = 'firstapp/show_cust.html'
    context = {'customers':all_cust}
    return render(request,template,context)


def addcust(request):
    if request.method =='POST':
        cust=customerform(request.POST)
        if cust.is_valid():
            n = cust.cleaned_data['name']
            c = cust.cleaned_data['city']
            p = cust.cleaned_data['phone']
            print(n,c,p)
            cust_obj = Customer1(name=n, city=c, phone=p)
            cust_obj.save()
        return redirect('/home/sc/')
    else:
        cust=customerform()
        template_name='firstapp/add_custdf.html'
        context= {'form':cust}
        return render(request,template_name,context)

def addorder(request):
    if request.method == 'POST':
        ord=orderform(request.POST)
        if ord.is_valid():
            ord.save()
        return redirect('/home/socf/')

    else:
        ord=orderform()
        template_name='firstapp/addord.html'
        context= {'form':ord}
        return render (request,template_name,context)


def all_order(request):
    all_ord = Orders.objects.all()
    template = 'firstapp/all_ord.html'
    context = {'orders':all_ord}
    return render(request,template,context)

