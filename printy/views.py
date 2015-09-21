from django.shortcuts import render, get_object_or_404
from printy.models import PrintPage


def print_view(request, print_page, model=True):
    print_page = get_object_or_404(PrintPage, pk=print_page)
    return render(request, 'print_model.html', locals())

