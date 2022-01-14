from django.urls import path, include
from . import views
from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)
router.register(r'scores', views.ScoreViewSet)

urlpatterns =[
    # path('candidate/<candidate_ref>/', views.get_candidate)  
    #incoming URL (request) , returned view
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]