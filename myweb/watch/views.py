from django.shortcuts import render, redirect
from django.http import HttpResponse
from watch.models import Item
from watch.forms import ItemForm
from users.models import CusOrders, CusRatingFeedback
from django.views.generic import TemplateView


# Create your views here.


def index(request, category=None):
    if category:
        itemlist = Item.objects.filter(category=category)
    else:
        itemlist = Item.objects.all()

    context = {
        'itemlist': itemlist,
        'selected_category': category,  # To highlight the selected category in the template
    }

    return render(request, 'watch/index.html', context)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    Obj_CusOrd = CusOrders.objects.filter(user=request.user)
    
    crf = CusRatingFeedback.objects.filter(
        prod_code=item.prod_code
    )

    context = {
        'item': item,
        'oco':Obj_CusOrd,
        'crf':crf
    }

    return render(request, 'watch/detail.html', context)

def create_item(request):

    form = ItemForm(request.POST or None)




    if form.is_valid():

        form.save()

        return redirect('watch:index')




    context = {

        'form':form

    }




    return render(request, 'watch/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('watch:index')

    return render(request, 'watch/item-form.html', context)

def delete_item(request, id):
    item = Item.objects.get(pk=id)

    context = {
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('watch:index')

    return render(request, 'watch/item-delete.html', context)

def mens(request):
    itemlist = Item.objects.filter(category='m')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'watch/mens.html', context)

def womens(request):
    itemlist = Item.objects.filter(category='f')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'watch/womens.html', context)

def kids(request):
    itemlist = Item.objects.filter(category='k')

    # for search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        itemlist = itemlist.filter(item_name__icontains=item_name)

    context = {
        'itemlist': itemlist
    }

    return render(request, 'watch/kids.html', context)



