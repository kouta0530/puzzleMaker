from django.shortcuts import render, redirect
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


def search_puzzle_data(request, search_words):
    puzzle_data = Puzzle.objects.all()
    if search_words:
        search_words = search_words.split()
        print(search_words)
        for word in search_words:
            puzzle_data = puzzle_data.filter(title__icontains=word)

        puzzle_data = list(puzzle_data.values())
        return HttpResponse(json.dumps(puzzle_data, ensure_ascii=False,
                                       default=str),
                            content_type='applicaion/json')
    else:
        return redirect('index')
