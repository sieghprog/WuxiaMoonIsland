from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel
from django.db.models import Q, Count, Case, When
from categories.models import Category

class IndexView(ListView):
    model = Novel
    template_name = 'index.html'
    vs = False
    context_object_name = 'novels'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().filter(novel_visible=True)
        qs = qs.order_by('-novel_updated')
        qs = qs.annotate(
            chapters_count=Count(
                Case(
                    When(chapter__chapter_visible=True, then=1)
                )
            )
        )
        return qs
class CategoriesList(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'

class CategoryView(CategoriesList):
    model = Category
    template_name = 'index.html'
    context_object_name = 'novels'
    def get_queryset(self):
        qs = super().get_queryset()
        print(self.kwargs.get('category_name', None))
        category = (self.kwargs.get('category_name', None))

        if not category:
            return qs


        qs = Novel.objects.filter(novel_categories__category_name=category, novel_visible=True)
        qs = qs.annotate(
            chapters_count=Count(
                Case(
                    When(chapter__chapter_visible=True, then=1)
                )
            )
        )
        print(Novel.objects.filter(novel_categories__category_name=category))
        return qs

class DetailsView(UpdateView):
    model = Novel
    template_name = 'novel_details.html'
