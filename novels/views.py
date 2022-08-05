from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Novel
from django.db.models import Q, Count, Case, When

class IndexView(ListView):
    model = Novel
    template_name = 'index.html'
    vs = False
    context_object_name = 'novels'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-novel_updated')
        qs = qs.annotate(
            chapters_count=Count(
                Case(
                    When(chapter__chapter_visible=True, then=1)
                )
            )
        )
        return qs


class CategoryView(IndexView):
    pass

class CategoriesList(ListView):
    pass

class DetailsView(UpdateView):
    pass
