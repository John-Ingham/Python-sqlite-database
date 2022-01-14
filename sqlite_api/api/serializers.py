from . models import Candidate, Score
from rest_framework import serializers

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ("id", "name", "candidate_ref")


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ("id", "score", "candidate_ref")

