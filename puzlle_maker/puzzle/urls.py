from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('puzzles/<int:id>', views.get_puzzle_data, name='get puzzle data'),
    path('puzzles/<str:search_words>',
         views.search_puzzle_data, name='search puzzle data')
]
