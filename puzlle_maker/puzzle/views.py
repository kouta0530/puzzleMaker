from django.shortcuts import render
from django.http import HttpResponse
from puzzle.models import Puzzle
# Create your views here.


def index(request):
    puzzle = Puzzle.objects.filter(pk__range=(1, 30))
    return render(request, './search_result.html', puzzle=puzzle)


def get_puzzle_data(request, id):
    return HttpResponse('get puzzle json array response')
