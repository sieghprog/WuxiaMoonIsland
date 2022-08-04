from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel

class IndexView(ListView):
    model = Novel
    template_name = 'index.html'


class CategoryView(IndexView):
    pass

class CategoriesList(ListView):
    pass

class DetailsView(UpdateView):
    pass
