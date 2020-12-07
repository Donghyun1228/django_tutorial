from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>', views.update, name='update'),
    path('<int:pk>', views.delete, name='delete'),
]