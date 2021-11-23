from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from puzzle.models import Puzzle
from puzzle.helper import create_index, more_than_specified_number
import json
# Create your views here.


def index(request):
    data = {'puzzle':
            list(Puzzle.objects.all().values())[:30]}
    return render(request, './search_result.html', data)


def get_puzzle_data(request, id):
    count = Puzzle.objects.all().count()
    end = more_than_specified_number(count, (id + 1) * 30)
    data = list(Puzzle.objects.filter().values())[id * 30:end]
    return HttpResponse(json.dumps(data, ensure_ascii=False, default=str),
                        content_type="application/json")


def search_puzzle_data(request):
    search_words = request.GET.get('search_words')
    id = int(request.GET.get('id')) if request.GET.get('id') else 1

    if search_words:
        search_words_list = search_words.split()

        q_objects = [Q(title__icontains=s) for s in search_words_list]
        query = q_objects.pop()
        for q in q_objects:
            query |= q

        puzzle_model = Puzzle.objects.filter(query)
        count = create_index(puzzle_model.count(), 30)
        next_or_end_works_index = more_than_specified_number(
            puzzle_model.count(), id*30)

        puzzle_data = {
            'puzzle':
            list(puzzle_model[(id - 1) * 30:next_or_end_works_index].values()),
            'search_words': search_words,
            'count': count
        }
        return render(request, './search_result.html', puzzle_data)
    else:
        return redirect('index')
