from django.shortcuts import render
from setting.models import Setting,Latest,Slid,Ders,Man,Woman,Kids,Nues,Insta,Closis
from setting.models import Phone
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    product = Latest.objects.all()
    slide = Slid.objects.latest('id')
    product1 = Ders.objects.all()
    product2 = Man.objects.all()
    product3 = Woman.objects.all()
    product4 = Kids.objects.all()
    nuser = Nues.objects.latest('id')
    prese = Insta.objects.latest('id')
    product5 = Closis.objects.all()

    

    context = {
        'setting' : setting,
        'product' : product,
        'slide' : slide,
        'product1' : product1,
        'product2' : product2,
        'product3' : product3,
        'product4' : product4,
        'nuser' : nuser,
        'prese' : prese,
        'product5' : product5
        
    }
    return render(request, 'index.html', context)

def phone(request):
    phone = Phone.objects.latest('id')

    context = {
        'phone' : phone
    }
    return render(request, 'contact.html', context)
