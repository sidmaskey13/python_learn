from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm
from .forms import RawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        # Product.objects.create(**form.cleaned_data)
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)


def product_edit_view(request,p_id):
    obj = get_object_or_404(Product, id=p_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        # Product.objects.create(**form.cleaned_data)
        form.save()
        form = ProductForm()
        return redirect('/products')
    context = {
        'form': form
    }
    return render(request, 'product/edit.html', context)


def product_show_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    # try:
    #     obj = Product.objects.get(id=p_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object': obj
    }
    return render(request, "product/show.html", context)


def product_delete_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/products')

    context = {
        "object": obj
    }
    return render(request, "product/delete.html", context)


def product_index_view(request):
    queryset = Product.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"product/index.html",context)
