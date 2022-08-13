from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

import novels.views
from chapters.models import Chapter
from .models import Novel
from django.db.models import Q, Count, Case, When
from categories.models import Category


class IndexView(ListView):
    model = Novel
    template_name = 'index.html'
    context_object_name = 'novels'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.order_by('category_name')
        print(context)
        return context

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
        category = (self.kwargs.get('category_name', None))

        if not category:
            return qs

        qs = Novel.objects.filter(novel_categories__category_name=category, novel_visible=True).annotate(
            chapters_count=Count(Case(When(chapter__chapter_visible=True, then=1)))
        )

        return qs

class DetailsView(DetailView):
    model = Novel
    template_name = 'novel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Chapters'] = Chapter.objects.filter(chapter_novel=self.get_object())

        return context



