from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product, Application
from .models import ConversationMessage #, Userprofile
from notification.utilities import create_notification


@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_seller:
    #if request.user.userprofile:
        application = get_object_or_404(Application, pk=application_id, product__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)
    
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            create_notification(request, application.created_by, 'message', extra_id=application.id)

            return redirect('view_application', application_id=application_id)
    
    return render(request, 'userprofile/view_application.html', {'application': application})

@login_required
def view_dashboard_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_product.html', {'product': product})
# Create your views here.
