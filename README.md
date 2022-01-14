# Python-sqlite-database

A python REST Api application using sqlite database.

### Welcome to my project.

To view the project live on a browser please fork and clone from the github repo, then if you have python3 installed use the command `python3 manage.py runserver`

### Installs used in the project:

Python3
Django 2.1.5
Django Rest Framework

### Endpoints:

##### Root - localhost:8000/api/

Shows the root Api and it's returns using the Django rest framework display.

##### Candidates - localhost:8000/api/candidates/

Shows a list of all candidates in the database and accepts a JSON object {"name" : "Candidate name",
"candidate_ref" : "9gf63hgt" }
Name max length 255 char, ref must be an 8 character identifier

##### Scores - localhost:8000/api/scores/

Shows a list of all scores held in the database and accepts a JSON object {"candidate_ref" : "9fg63hgt", "score" : 76}
Candidate ref must be an 8 character identifier, score must be a float number between 0 and 100.
