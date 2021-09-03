from django.shortcuts import render
from django.http import HttpResponse
from puzzle.models import Puzzle
# Create your views here.


def index(request):
    data = {'puzzle': list(
        Puzzle.objects.filter(pk__range=(1, 30)).values())}
    return render(request, './search_result.html', data)


def get_puzzle_data(request, id):
    return HttpResponse('get puzzle json array response')
