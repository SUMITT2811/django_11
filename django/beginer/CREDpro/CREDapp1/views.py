from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoes 

def saveShoes(request):
    if request.method =='POST':
        sname = request.POST['sName']
        sbrand = request.POST['sBrand']
        size = request.POST['size']
        stype = request.POST['sType']
        price = request.POST['price']
        status=request.POST['status']
        new_shoes=Shoes(sName=sname,sBrand=sbrand,size=size,sType=stype,price=price,status=status)
        Shoes.save(new_shoes)
        print(new_shoes) 
        return HttpResponse('<h1> success..... </h1>')

    else:
        return render(request,'index.html')   


def getALLShoes(request):
    shoelist = Shoes.objects.all()
    return render(request, 'Showlist.html', {'slist': shoelist})  

def updateShoes(request):
    if request.method =='POST':
        sname = request.POST['sName']
        sbrand = request.POST['sBrand']
        size = request.POST['size']
        stype = request.POST['sType']
        price = request.POST['price']
        status=request.POST['status'] 
        data=Shoes.objects.get(sId=shoe_id)
        data.update(sname=name, sprice=price,sBrand=Brand, size=size, stype=stype,)
        return HttpResponse('<h1> success </h1>')
    else:
        return render(request,'updateshoe.html')       