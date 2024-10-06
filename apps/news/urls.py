from django.urls import path
from .views import NewsListAPI, NewsCreateAPI, NewsRetriveAPI

urlpatterns = [
    path('', NewsListAPI.as_view(), name='news list api'),
    path('create/', NewsCreateAPI.as_view(), name='news create api'),
    path('retrive/<int:pk>', NewsRetriveAPI.as_view(), name='news retrive api'),

]