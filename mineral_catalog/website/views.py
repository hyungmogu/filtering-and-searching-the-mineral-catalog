from django.shortcuts import render, get_object_or_404, redirect
import random

from .models import Mineral

# Create your views here.


def home_page(request):
    # import all items from database
    minerals = Mineral.objects.all()

    # load items to view
    return render(request, 'website/home_page.html', {'minerals': minerals})


def mineral_detail(request, mineral_pk):
    # fetch specific object based on pk
    mineral = get_object_or_404(Mineral, pk=mineral_pk)

    # load item to view
    return render(request, 'website/detail.html', {'mineral': mineral})


def random_mineral(request):
    random.seed()

    # get all minerals
    minerals_cnt = Mineral.objects.count()

    # from all minerals randomly pick one in between range of 0
    # to the length of file
    pk = random.randint(1, minerals_cnt)

    # redirect to mineral detail page
    return redirect(mineral_detail, mineral_pk=pk)