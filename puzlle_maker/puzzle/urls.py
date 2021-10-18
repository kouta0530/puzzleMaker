from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('puzzles/',
         views.search_puzzle_data, name='search puzzle data'),
    path('puzzles/<int:id>', views.get_puzzle_data, name='get puzzle data'),
]
