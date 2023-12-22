from django.shortcuts import render, redirect
from django.http import HttpResponse
from watch.models import Item
from watch.forms import ItemForm
from users.models import CusOrders, CusRatingFeedback

# Create your views here.

def index(request):
    
   
    itemlist = Item.objects.all()

   

    

        
    

    context = {
        'itemlist': itemlist
    }

    return render(request, 'watch/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    Obj_CusOrd = CusOrders.objects.all()
    
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

def delete_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(pk=crf_id)

    context = {
        'crfo':crfo
    }

    if request.method == 'POST':
        crfo.delete()
        return redirect('food:detail', item_id=details_id)

    return render(request, 'users/crf_del.html', context)