from django.shortcuts import render, HttpResponse, redirect
from .models import product

# Create your views here.

def index(request):
    # abc = product.objects.all()
    abc = product.objects.filter(status = False)


    # return HttpResponse("Hello World")
    return render(request, 'index.html', {'abc' : abc})
    # pass
  
def store(request):
    if request.method =="POST":
        a = request.POST.get('product_name')
        b = request.POST.get('product_price')
        c = request.POST.get('product_qtt')

        # print(a)
        # print(b)
        # print(c)

        xyz = product(
            product_name = a,
            product_price = b,
            product_qtt = c
            
        )
        xyz.save()
        return redirect('showdata')

    return render(request, 'store.html')

def edit_db(request,id):
    product_edit = product.objects.filter(id=id)
    return render(request,'edit.html',{'product_edit' : product_edit})

def product_update(request, id):
    if request.method =="POST":
        a = request.POST.get('product_name')
        b = request.POST.get('product_price')
        c = request.POST.get('product_qtt')

        xyz = product.objects.filter(id=id)
        xyz = product(
            id = id,
            product_name = a,
            product_price = b,
            product_qtt = c
            
        )
        xyz.save()
        return redirect('showdata')
    
def delete_product(request,id):
    del_product = product.objects.filter(id=id).delete()
    return redirect ('showdata')

def task_done(request,id):
    task_complete =  product.objects.get(id=id)
    task_complete.status = True
    task_complete.save()
    return redirect('showdata')

def task_incomplete(request,id):
    task_incomplete =  product.objects.get(id=id)
    task_incomplete.status = False
    task_incomplete.save()
    # task_incomplete = product.objects.get(id=id)
    # return render(request,'index.html',{'task_incomplete' : task_incomplete})
    return redirect('showdata')
    


        
