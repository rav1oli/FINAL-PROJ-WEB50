from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from .models import Problem, ProblemSet, PROBLEMS_SORTABLE_BY
from .serializers import ProblemSerializer, ProblemSetSerializer


# index route should display pages from public users by default, 
def index(request):
    return render(request, "maths/index.html")


def createProblem(request):
    return render(request, "maths/create_problem.html")


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def problem_sets(request, subset="public", order="-time_created",):
    
    if order not in PROBLEMS_SORTABLE_BY:
        return HttpResponse({"error": "Invalid query order"})
    
    if subset == "public":
        sets = ProblemSet.objects.all().order_by(order).prefetch_related('problems')[:1000]
    elif subset == "personal":
        sets = ProblemSet.objects.filter(user=request.user).order_by(order).prefetch_related('problems')[:1000]

    
    serializer = ProblemSetSerializer(sets, many=True)

    return Response(serializer.data)



    