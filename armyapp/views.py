# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Sum,Count
from datetime import date,timedelta
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from .models import stock,issueregister,loadchart

@login_required(login_url='/login')
def homepage(request):

    tl=stock.objects.aggregate(Sum('quantityrecieved'))['quantityrecieved__sum']
    tq = stock.objects.aggregate(Count('materialno'))['materialno__count']
    tli = issueregister.objects.aggregate(Sum('issueqty'))['issueqty__sum']


    return render(request,"index.html",{'header':'Army Logistics','tll':tl,'tli':tli,'tqq':tq,'htitle':'Load Management & Traffic'})


@login_required(login_url='/login')
def addnew(request):
        return render(request, "addnewform.html",{'header':'Army Logistics','htitle':'Load Management & Traffic'})


def login(request):
    return render(request, "login.html")


@login_required(login_url='/login')
def addstock(request):
    materialno = request.POST['materialno']
    nomenclature = request.POST['nomenclature']
    quantity = request.POST['quantity']
    ratio = request.POST['ratio']
    subdepo = request.POST['subdepo']
    if stock.objects.filter(materialno=materialno).exists():
        messages.success(request, 'Material No. Already Exists ')

        return HttpResponseRedirect('/addnew')

    p = stock(materialno=materialno, nomenclature=nomenclature,quantityrecieved=quantity,wtratio=ratio,subdepot=subdepo)
    p.save()
    messages.success(request, 'Item Added successfully ')

    return HttpResponseRedirect('/stocktable')


def test(request):
    return HttpResponse("success")


@login_required(login_url='/login')
def stocktable(request):
    stocklist=stock.objects.all()
    return render(request,"stocktable.html",{'stocks':stocklist,'title':'Stock Table','header':'Army Logistics','htitle':'Load Management & Traffic'})



@login_required(login_url='/login')
def issueregistershow(request):
    issuelist = issueregister.objects.all()
    return render(request,"issueregister.html",{'issue':issuelist,'header':'Army Logistics','htitle':'Load Management & Traffic'})



@login_required(login_url='/login')
def issueaction(request,userid):
    item = stock.objects.get(materialno=userid)
    return render(request,"issueform.html",{'title':'Issue Form','header':'Army Logistics','itemdata':item,'htitle':'Load Management & Traffic'})


@login_required(login_url='/login')
def deposhow(request,depoid):
    depoid1=int(depoid)
    item = stock.objects.all().filter(subdepot=depoid1)
    return render(request,"depo.html",{'title':'Sub Depot','header':'Army Logistics','stocks':item,'htitle':'Load Management & Traffic'})


@login_required(login_url='/login')
def submitissue(request):
    materialno = request.POST['materialno']
    nomenclature = request.POST['nomenclature']
    quantityheld = request.POST['quantityheld']
    issuequantity = request.POST['issuequantity']
    unit = request.POST['unit']
    depo = request.POST['depo']
    idate = date.today()

    if int(quantityheld)<int(issuequantity):
        messages.success(request, 'Issue Quantity is greater than available quantity.')
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    quantityfinal=int(quantityheld)-int(issuequantity)

    stock.objects.filter(materialno=materialno).update(quantityrecieved=quantityfinal)

    p = issueregister(materialno=materialno, nomenclature=nomenclature,quantityheld=quantityfinal,
                      issueqty=issuequantity,subdepot=depo,unit=unit,issuedate=idate)
    p.save()

    if depo=='1':
        oldsd1= loadchart.objects.only('sd1').get(unit=unit).sd1
        oldload=loadchart.objects.only('totalload').get(unit=unit).totalload
        newload=oldload+int(issuequantity)
        newsd1= oldsd1+int(issuequantity)
        edate= idate +timedelta(days=9)
        loadchart.objects.filter(unit=unit).update(expdate=edate,sd1=newsd1,d1=idate,totalload=newload)

    if depo=='2':
        oldsd2= loadchart.objects.only('sd2').get(unit=unit).sd2
        oldload = loadchart.objects.only('totalload').get(unit=unit).totalload
        newload = oldload + int(issuequantity)
        newsd2= oldsd2+int(issuequantity)
        edate= idate +timedelta(days=10)
        loadchart.objects.filter(unit=unit).update(expdate=edate,sd2=newsd2,d2=idate,totalload=newload)



    if depo=='3':
        oldsd3 = loadchart.objects.only('sd3').get(unit=unit).sd3
        oldload = loadchart.objects.only('totalload').get(unit=unit).totalload
        newload = oldload + int(issuequantity)
        newsd3= oldsd3+int(issuequantity)
        edate= idate +timedelta(days=10)
        loadchart.objects.filter(unit=unit).update(expdate=edate,sd3=newsd3,d3=idate,totalload=newload)

    if depo=='4':
        oldsd4 = loadchart.objects.only('sd4').get(unit=unit).sd4
        oldload = loadchart.objects.only('totalload').get(unit=unit).totalload
        newload = oldload + int(issuequantity)
        newsd4= oldsd4+int(issuequantity)
        edate= idate +timedelta(days=12)
        loadchart.objects.filter(unit=unit).update(expdate=edate,sd4=newsd4,d4=idate,totalload=newload)

    messages.success(request, 'Material Issued Successfuly')
    return HttpResponseRedirect('/issueregister',)




@login_required(login_url='/login')
def loadchartshow(request):
    unitlist = loadchart.objects.all()
    return render(request,"loadchart.html",{'loaddata':unitlist,'header':'Army Logistics','htitle':'Load Management & Traffic'})




def loginaction(request):
    loginid = request.POST['loginid']
    password = request.POST['password']
    c=auth.authenticate(username=loginid,password=password)
    if c is None:
        messages.success(request, 'Invalid ID or Password ')
        return HttpResponseRedirect('/login')
    else:
        auth.login(request,c)
        messages.success(request, 'Login Successful')
        return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out Successfully')
    return HttpResponseRedirect('/login')


