from django.db import models # imports the models class information
from django.core.validators import MaxValueValidator, MinValueValidator

# Model will save data to the database, using ORM, object relational mapping
# Avoids writing SQL, Django does this for us.

## Required classes CANDIDATE and SCORE
# Candidate will contain `name` and `candidate reference`
# Score will contain `score`    

class Candidate(models.Model):
    name = models.CharField(max_length = 255) ## no limit on characters, but prevents long string injection
    candidate_reference = models.CharField(max_length = 8) # Will always be an unique 8 character code


class Score(models.Model):
    score = models.FloatField(min = 0.0, max = 100.0, validators = [MinValueValidator(0.0), MaxValueValidator(100.0)]) # Will always be a float number between 1 and 100
    candidate_reference = models.CharField(max_length = 8)

    ##Added candidate reference to score class so that a request for all that candidates scores is possible.
