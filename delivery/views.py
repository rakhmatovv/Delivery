from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')


def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("delivery:delivery_list")  # Используем именованный URL 'delivery'
    else:
        form = DeliveryForm()

    return render(request, 'delivery.html', {'form': form})


def delivery_list(request):
    orders = Location.objects.all()
    return render(request, 'delivery_list.html', {"orders":orders})