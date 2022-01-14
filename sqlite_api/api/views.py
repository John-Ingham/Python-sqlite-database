from django.shortcuts import render
from django.http import HttpResponse
from . models import Candidate, Score
from rest_framework import viewsets
from . serializers import CandidateSerializer, ScoreSerializer




## Views, return to user

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
# Will handle a return of `all` scores - need to edit this

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
# Will handle a return of all candidates


def get_candidate(request, candidate_ref=None):
    message = f'You submitted candidate ref {candidate_ref}'
    return HttpResponse(message)

    scores = Score.objects.all({candidate_ref})

    return render(request, "index.html", {"score": scores})