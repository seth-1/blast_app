from django.urls import path

from . import views

app_name = 'blast_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('results', views.ResultsView.as_view(), name='results'),
    path('blast_request/', views.blast_request, name='blast_request'),
]