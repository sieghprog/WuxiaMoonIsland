from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('category/<str:category_name>', views.CategoryView.as_view(), name='category_view'),
    path('category_list/', views.CategoriesList.as_view(), name='category_list'),
    path('search/', views.IndexView.as_view(), name='search_view'),
    #aula 4 busca
    path('details/<int:pk>', views.DetailsView.as_view(), name='details_view'),

]