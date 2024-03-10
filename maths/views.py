import json

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Prefetch
from rest_framework.response import Response
from .models import *


# index route should display pages from public users by default, 
def index(request):
    return render(request, "maths/index.html")


def createProblem(request):
    return render(request, "maths/create_problem.html")


def public_sets(request, order="-time_created",):
    
    if order not in PROBLEMS_SORTABLE_BY:
        return HttpResponse({"error": "Invalid query order"})
    
    sets = ProblemSet.objects.all().order_by(order).prefetch_related('problems')[:1000]
    
    serializer = ProblemSetSerializer(sets, many=True)

    return JsonResponse({'sets': serializer.data, 'message': "All good",}, status=201)



    
def my_sets(request, order="-time_created",):
    if order not in PROBLEMS_SORTABLE_BY:
        return HttpResponse({"error": "Invalid query order"})
    
    sets = ProblemSet.objects.filter(user=request.user).order_by(order).prefetch_related('problems')[:1000]
    
    serializer = ProblemSetSerializer(sets, many=True)

    return JsonResponse({'sets': serializer.data, 'message': "All good",}, status=201)



    