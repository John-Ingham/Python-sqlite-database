from django.contrib import admin
from . models import Candidate, Score # Import models 

# Register your candidate and score models here to be able to see them in the admin section of the application

admin.site.register(Candidate)
admin.site.register(Score)
