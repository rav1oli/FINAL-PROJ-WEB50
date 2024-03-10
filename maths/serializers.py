from .models import *
from rest_framework import serializers


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProblemSet
        fields = '__all__'

    problems = ProblemSerializer(many=True)
