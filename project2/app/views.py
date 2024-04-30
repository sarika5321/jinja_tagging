from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('ename')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        EO = Emp(ename = name, pno = pno, email = email, add = add )
        EO.save()
        return HttpResponse("Register successfully.")
    return render(request, 'register.html')

def home(request):
    EO = Emp.objects.all()
    d={'Employeeobjects':EO}
    
    return render(request, 'home.html', d)

