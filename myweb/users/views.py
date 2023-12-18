from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('watch:index')

    else:
        form = RegisterForm()

        context = {
            'form':form
        }

        return render(request, 'users/register.html', context)