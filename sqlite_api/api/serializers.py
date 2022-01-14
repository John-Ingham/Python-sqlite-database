from . models import Candidate, Score
from rest_framework import serializers

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ("name", "candidate_reference")


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ("score", "candidate_reference")

        