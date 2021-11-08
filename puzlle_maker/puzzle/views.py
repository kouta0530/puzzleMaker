from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from puzzle.models import Puzzle
from puzzle.helper import create_index
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


def search_puzzle_data(request):
    search_words = request.GET.get('search_words')

    if search_words:
        search_words = search_words.split()

        q_objects = [Q(title__icontains=s) for s in search_words]
        query = q_objects.pop()
        for q in q_objects:
            query |= q

        puzzle_model = Puzzle.objects.filter(query)

        puzzle_data = {'puzzle': list(
            puzzle_model.values()), 'count': create_index(len(puzzle_model))}
        return render(request, './search_result.html', puzzle_data)
    else:
        return redirect('index')
