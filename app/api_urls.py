from django.urls import path
from .views import SchoolListView, ShoolCreateView
    
urlpatterns = [
    path('schools/', SchoolListView.as_view(), name='school-list'),
    path('schools/create/', ShoolCreateView.as_view(), name='school-create'),
]       