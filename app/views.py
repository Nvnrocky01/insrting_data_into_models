from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

def school(request):
    if request.method == 'POST':
        sn=request.POST['sn']
        sp=request.POST.get('sp')
        sl=request.POST.get('sl')
        so=School.objects.get_or_create(sname=sn,sprincipal=sp,slocation=sl)[0]
        so.save()
        return HttpResponse('school data is inserted')
    return render(request,'create_school_school.html')