from django.shortcuts import render

def displayform(request):
    return render(request, 'addemployee.html')

def saveEmp(request):
    if request.method=='POST':
        Id=request.POST['eId']
        Name=request.POST['fname']
        Email=request.POST['email']
        Password=request.POST['password']
        Address=request.POST['address']
        Contact=request.POST['contact']
        print(Id)
        print(Name)
        print(Email)
        print(Password)
        print(Address)
        print(Contact)
    return render(request, 'success.html')