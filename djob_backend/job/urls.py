from django.urls import path

from . import views

urlpatterns = [
    path('', views.BrowseJobsView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('newest/', views.NewesetJobsView.as_view()),
    path('<int:pk>/', views.JobsDetailView.as_view()),
]
