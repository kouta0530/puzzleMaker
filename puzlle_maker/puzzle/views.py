from django.shortcuts import render
from django.http import HttpResponse
from puzzle.models import Puzzle
import json
# Create your views here.


def index(request):
    data = {'puzzle':
            list(Puzzle.objects.all().values())[:30]}
    return render(request, './search_result.html', data)


def get_puzzle_data(request, id):
    count = Puzzle.objects.all().count()
    end = (id + 1) * 30 if (id + 1) * 30 <= count else count
    data = list(Puzzle.objects.filter().values())[id * 30:end]
    return HttpResponse(json.dumps(data, ensure_ascii=False, default=str),
                        content_type="application/json")
