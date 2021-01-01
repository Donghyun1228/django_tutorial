from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', views.index, name='index'),

    # /blog/create/
    path('create/', views.create, name='create'),

    # /blog/<int>/
    path('<int:post_id>/', views.detail, name='detail'),

    # /blog/<int>/update
    path('<int:post_id>/update/', views.update, name='update'),
    
    # /blog/<int>/delete
    path('<int:post_id>/delete/', views.delete, name='delete'),
]