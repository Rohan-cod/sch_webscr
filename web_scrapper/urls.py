from django.urls import path

from .views import JobListView, HomePageView, JobDetailView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('<int:pk>/',
         JobDetailView.as_view(), name='job_detail'),
    path('search/', search_view, name='search'),
]