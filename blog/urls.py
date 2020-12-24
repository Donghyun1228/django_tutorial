from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
]