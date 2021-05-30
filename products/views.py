from django import forms
from django.http import request, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .form import ProductForm, RawProductForm

from .models import Product


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }

    return render(request, "products/product_list.html", context)


#Deleting a product
def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id= my_id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object' : obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'obj' : obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'Title': 'My Title'
        , 'Description': 'Desc'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm()
#     if(request.method == 'POST'):
#         my_form = RawProductForm(request.POST)

#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form' : my_form
#     }   
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print(request.GET)
#     #print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         #Product.objects.create(title=my_new_title)

#     context = {
#     }   
#     return render(request, "products/product_create.html", context)



def product_create_view(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }   
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj' : obj
    }
    return render(request, "products/product_detail.html", context)
