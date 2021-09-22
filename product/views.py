from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from .forms import AddProductForm, ApplicationForm
from .models import Product

from notification.utilities import create_notification

def search_p(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(company_url__contains=searched)

        return render(request, 'product/search_product.html',{'searched':searched, 'products':products})
    else:
        return render(request, 'product/search_product.html' )

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    return render(request, 'product/product_detail.html', {'product': product})

@login_required
def apply_for_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.product = product
            application.created_by = request.user
            application.save()

            create_notification(request, product.created_by, 'application', extra_id=application.id)

            return redirect('dashboard')
    else:
        form = ApplicationForm()
    
    return render(request, 'product/apply_for_product.html', {'form': form, 'product': product})

@login_required
def add_product(request):
    user = request.user
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        #image = request.FILES.getlist('image')
        if form.is_valid():            
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect('dashboard')
    else:
        form = AddProductForm()
        
    return render(request, 'product/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, created_by=request.user)

    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            product = form.save(commit=False)
            product.status = request.POST.get('status')
            product.save()

            return redirect('dashboard')
    else:
        form = AddProductForm(instance=product)
    
    return render(request, 'product/edit_product.html', {'form': form, 'product': product})
