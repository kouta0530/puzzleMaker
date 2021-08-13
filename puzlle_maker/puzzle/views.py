from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, './search_result.html')


def get_puzzle_data(request, id):
    return HttpResponse('get puzzle json array response')
