from django.shortcuts import render
from django.http import HttpResponse
from . models import Candidate, Score
from rest_framework import viewsets
from . serializers import CandidateSerializer, ScoreSerializer




## Views, return to user

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
# Will handle a return GET of `all` scores and receive a POST


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
# Will handle a return GET of all candidates and eceive a POST


