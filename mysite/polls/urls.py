from django.urls import path
from . import views

app_name = 'polls'

# To call the view, we need to map it to a URL: url mapping
urlpatterns = [
    path('', views.index, name='index'),
    path('first', views.index, name='index1'),
    path('second', views.index, name='index2'),
    path('third', views.anotherindex, name='anotherindex'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # ex: /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
]