from django.contrib import admin
from django.urls import path, re_path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail'),
    path('create/', views.SchoolCreateView.as_view(), name = 'create'),
    path('<int:pk>/update/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', views.SchoolDeleteView.as_view(), name = 'delete')
]
