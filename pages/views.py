from django.shortcuts import render, get_object_or_404

from .models import Page
# Create your views here.

def page(request, pk, page_slug):
    page = get_object_or_404(Page, id=pk)

    return render(request, 'pages/sample.html', {'page': page})