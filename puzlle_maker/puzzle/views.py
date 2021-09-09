from django.shortcuts import render
from django.http import HttpResponse
from puzzle.models import Puzzle
import json
# Create your views here.


def index(request):
    data = {'puzzle': list(
        Puzzle.objects.filter(pk__range=(1, 30)).values())}
    return render(request, './search_result.html', data)


def get_puzzle_data(request, id):
    data = list(Puzzle.objects.filter(pk__range=(id + 1, id + 30)).values())

    return HttpResponse(json.dumps(data, ensure_ascii=False, default=str),
                        content_type="application/json")
