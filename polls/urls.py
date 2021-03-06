from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
# 함수 기반 뷰 url
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]

# 클래스 기반 뷰 url
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/result', views.ResultView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote')

