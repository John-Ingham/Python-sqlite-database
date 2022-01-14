from . models import Candidate, Score
from rest_framework import serializers

#serializers convert json to data and vice versa 


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ("name", "candidate_ref")


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ("score", "candidate_ref")

