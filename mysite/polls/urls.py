from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"), # http://127.0.0.1:8000/polls/
    path('<int:question_id>/', views.detail, name="detail"), # http://127.0.0.1:8000/polls/1
    path('<int:question_id>/results/', views.results, name="results"), # http://127.0.0.1:8000/polls/1/results
    path('<int:question_id>/vote/', views.vote, name="vote"), # http://127.0.0.1:8000/polls/1/vote
]
