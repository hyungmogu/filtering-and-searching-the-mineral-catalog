from django.shortcuts import render, get_object_or_404, redirect
import random

from .models import Mineral


# Create your views here.
def home_page(request):
    # initialize
    alphabets = [chr(x) for x in range(97, 123)]
    group = Mineral.objects.order_by('group').values('group').distinct()

    # get queries if exists
    q = request.GET.get('q', '')
    q_by_group = request.GET.get('q_by_group', '')
    q_by_text = request.GET.get('q_by_text', '')

    if q:
        minerals = Mineral.objects.filter(
            name__istartswith=q
        ).order_by(
            'name'
        ).values(
            'id', 'pk', 'name'
        )

    elif q_by_text:
        minerals = Mineral.objects.filter(
            name__icontains=q_by_text
        ).order_by(
            'name'
        ).values(
            'id', 'pk', 'name'
        )

    elif q_by_group:
        minerals = Mineral.objects.filter(
            group__iexact=q_by_group
        ).order_by(
            'name'
        ).values(
            'id', 'pk', 'name'
        )

    else:
        # import all items from database
        try:
            minerals = Mineral.objects.all()
        except Mineral.DoesNotExist:
            minerals = []

    # load items to view
    return render(request, 'website/home.html', {
        'minerals': minerals,
        'alphabets': alphabets,
        'group': group,
        'selected_group': q_by_group,
        'selected_letter': q
        })


def mineral_detail(request, mineral_pk):
    alphabets = [chr(x) for x in range(97, 123)]

    group = Mineral.objects.order_by('group').values('group').distinct()

    q_by_group = request.GET.get('q_by_group', '')
    q_by_text = request.GET.get('q_by_text', '')
    q_by_letter = request.GET.get('q', '')

    if q_by_group:
        # redirect to homepage with the query parameter
        return redirect('/?q_by_group={0}'.format(q_by_group))
    elif q_by_text:
        return redirect('/?q_by_text={0}'.format(q_by_text))
    elif q_by_letter:
        # redirect to homepage with the query parameter
        return redirect('/?q={0}'.format(q_by_letter))

    # fetch specific object based on pk
    mineral = get_object_or_404(Mineral, pk=mineral_pk)

    # load item to view
    return render(request, 'website/detail.html', {
        'alphabets': alphabets,
        'mineral': mineral,
        'group': group
    })


def random_mineral(request):
    random.seed()

    # get all minerals
    minerals_cnt = Mineral.objects.count()

    # from all minerals randomly pick one in between range of 0
    # to the length of file
    pk = random.randint(1, minerals_cnt)

    # redirect to mineral detail page
    return redirect(mineral_detail, mineral_pk=pk)