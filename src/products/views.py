from django.http import Http404
from django.shortcuts import render , get_object_or_404, redirect

from .models import Product
from .form import ProductForm

list_view = 'http://127.0.0.1:8000/product/'


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'product/product_list.html',context)

def product_add_view(request):
    # print(request.GET) 
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product_add.html", context)


def product_remove_view(request, product_id):
    context={}
    obj = get_object_or_404(Product, id = product_id) # this is used instead of Http404
    if request.method == "POST":
        obj.delete() #confirming delete
        return redirect(list_view)
    context['object']=obj

    return render(request,'product/product_remove.html',context)


def dynamic_detail_view(request,product_id):
    context={}
    try:
        obj = Product.objects.get(id=product_id)
        context['object']=obj

    except Product.DoesNotExist:
        raise Http404
    
    return render(request, 'product/product_detail.html',context) 


# INITIAL Practice
def home_view(request):
    # Here it gets a request as soon as
    # django detecs the 'home' in url
    print(request.user)  # return HttpResponse("<h1>Hello World</h1>")
    my_context = {
        "my_text": "This is me",
        "my_number": 123,
        "my_list": [123, 456, 321, "ABC"]
    }
    return render(request, "home.html", my_context)
