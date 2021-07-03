from django.shortcuts import render
from page.models import Post
from django.contrib import messages
# Create your views here.

def hello(request):
    tag = ['น้ำตก','ธรรมชาติ','หน้าฝน']
    return render(request,'index.html',
    {
        'name':'บทความ',
        'writer':'ผู้เขียน',
        'tags': tag
    })




def addPage(request):
    if request.method=='POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('passport') and request.POST.get('tel') and request.POST.get('country') and request.POST.get('comeform') and request.POST.get('district') and request.POST.get('canton')and request.POST.get('terminus') and request.POST.get('ldistrict') and request.POST.get('lcanton') and request.POST.get('image'):
            saverecord = Post()
            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.passport=request.POST.get('passport')
            saverecord.tel=request.POST.get('tel')
            saverecord.country=request.POST.get('country')
            saverecord.comeform=request.POST.get('comeform')
            saverecord.district=request.POST.get('district')
            saverecord.canton=request.POST.get('canton')
            saverecord.terminus=request.POST.get('terminus')
            saverecord.ldistrict=request.POST.get('ldistrict')
            saverecord.lcanton=request.POST.get('lcanton')
            saverecord.image=request.POST.get('image')
            saverecord.save()
            messages.success(request,'บันทึกเรียบร้อย')
            return render(request,'result.html')
    else:
            return render(request,'reuslt.html')
