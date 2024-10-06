from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer

# Create your views here.
class NewsListAPI(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsCreateAPI(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsRetriveAPI(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
