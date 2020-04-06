from django.urls import path
<<<<<<< HEAD
from  . import views
urlpatterns = [
    path('',views.index,name = 'index'),
]
=======
from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:question_id>/',views.detail,name = 'detail'),
    path('<int:question_id>/results/',views.results,name ='results'),
    path('<int:question_id>/vote/',views.vote,name = 'vote')
]
>>>>>>> 2020.4.6_only_vote
