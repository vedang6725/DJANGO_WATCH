from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import CusOrders, CusRatingFeedback
from users.forms import CusOrdersUpd, CusRatFeedForm
from django.http import JsonResponse
import json

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
           username = form.cleaned_data.get('username')
           messages.success(
                request, 
                'Welcome {}, your account has been successfully created.Now you may log in'.format(username)
            )
           form.save()
        return redirect('login')

    else:
        form = RegisterForm()

        context = {
            'form':form
        }

        return render(request, 'users/register.html', context)
    

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(
                request,
                'Invalid Login, try again'
            )
            return redirect('login')

        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Welcome Superuser {}, you have been successfully logged in'.format(request.user.username)
            )
            return redirect('watch:index')

        elif user is not None:
            login(request, user)
            messages.success(
                request,
                'Welcome {}, you have been successfully logged in'.format(request.user.username)
            )
            return redirect('watch:index')

    return render(request, 'users/login.html')

def logout_view(request):
    messages.success(
        request,
        '{}, you have successfully logged out'.format(request.user.username)
    )
    logout(request)
    return redirect('watch:index')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

def Orders(request, id, pdcd, user):

    context = {
        'pdcd':pdcd,
        'user':user
    }

    if request.method == 'POST':

        Obj_CusOrds = CusOrders(
            prod_code=pdcd,
            user=user,
            quantity=request.POST.get('qty')
        )

        Obj_CusOrds.save()

        return redirect('watch:detail', item_id=id)

    return render(request, 'users/orders.html', context)

def update_orders(request, id, upd_order_id):

    coo = CusOrders.objects.get(order_id=upd_order_id)
    form = CusOrdersUpd(request.POST or None, instance=coo)

    context = {
        'form':form
    }

    if request.method == 'POST':
        form.instance.order_id = coo.order_id
        form.instance.prod_code = coo.prod_code
        form.instance.user = request.user.username
        
        
        
        
        
        form.save()
        return redirect('watch:detail', item_id=id)

    return render(request, 'users/orders_upd.html', context)

def CusRatFeed(request, it_id, pc):

    form = CusRatFeedForm(request.POST or None)

    context = {
        'form':form
    }

    if request.method == 'POST':
        form.instance.prod_code = pc
        form.instance.username = request.user.username
        form.save()
        return redirect('watch:detail', item_id=it_id)

    return render(request, 'users/item-form.html', context)

def update_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(pk=crf_id)
    form = CusRatFeedForm(request.POST or None, instance=crfo)

    context = {
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('watch:detail', item_id=details_id)

    return render(request, 'users/crf_upd.html', context)

def delete_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(pk=crf_id)

    context = {
        'crfo':crfo
    }

    if request.method == 'POST':
        crfo.delete()
        return redirect('watch:detail', item_id=details_id)

    return render(request, 'users/crf_del.html', context)

def Payment(request, amt, qnt):

    context = {
        'amt':amt,
        'qnt':qnt,
        'tot':amt * qnt
    }

    return render(request, 'users/payment.html', context)


def OnApprove(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)

        context = {

        }

        return JsonResponse(context)


def PaymentSuccess(request):

    return render(request, 'users/pymtsuccess.html')