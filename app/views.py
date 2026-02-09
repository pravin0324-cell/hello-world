from django.http import HttpResponse
from django.shortcuts import render
from .models import School
from .serializers import SchoolSerializer
from rest_framework.generics import ListAPIView

def index(request):
    return HttpResponse("Hello, world pravin!\n")


class SchoolListView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer