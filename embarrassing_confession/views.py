from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Confession
from .serializers import ConfessionSerializer


def index(request):
    return render(request, 'index.html', {})


def get_confession(request):
    confession_list = Confession.objects.all()
    serialize = ConfessionSerializer(confession_list, many=True)
    print(serialize.data)
    return JsonResponse(serialize.data, safe=False)

