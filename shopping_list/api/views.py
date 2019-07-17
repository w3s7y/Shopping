from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest
import api.models
import json



def list(request):
    if request.method == "GET":
        return _get_list(request)
    elif request.method == "POST":
        return _post_list(request)
    elif request.method == "UPDATE":
        return _update_list(request)
    elif request.method == "DELETE":
        return _delete_list(request)
    else:
        return HttpResponseBadRequest("")


def _get_list(request):
    list = api.models.List.objects.get(pk=request.GET['owner_id'])
    return render(request, "list/list.json", {'list': list})


def _post_list(request):
    return HttpResponseBadRequest()


def _update_list(request):
    pass


def _delete_list(request):
    pass


def shop(request):
    user_list = api.models.List.objects.get(pk=request.GET['list_id'])
    return render(request, "list/list.json", {'list': user_list})




def item(request):
    pass


def offer(request):
    pass


def favorite(request):
    pass
