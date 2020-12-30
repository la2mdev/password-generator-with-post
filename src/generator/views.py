from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PasswordGenerator


def password_generator(request):
    
    form = PasswordGenerator(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        password = form.save()
        messages.success(request, password)

        return redirect('generator:password_generator')

    context = {'form': form}
    return render(request, 'index.html', context)
