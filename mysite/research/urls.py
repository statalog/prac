from django.urls import path
from . import views

app_name = 'research'
urlpatterns = [
    # ex: /explore/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /explore/5/
    path('upload/', views.UploadView.as_view(), name='upload'),
    # ex: /explore/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
]