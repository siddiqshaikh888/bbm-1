from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.models import Group, User

from product.models import Product
from userprofile.models import Userprofile

def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE).order_by('-created_at')[0:3]

    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'buyer')
            is_agree = request.POST.get('is_agree', 'checked')

            if account_type == 'seller':
                userprofile = Userprofile.objects.create(user=user, is_seller=True)
                userprofile.save()
            elif account_type == 'buyer':
                userprofile = Userprofile.objects.create(user=user, is_buyer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})

# Create your views here.
