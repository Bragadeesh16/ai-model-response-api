from django.urls import path
from myapp.views import *

urlpatterns = [
    path('api/responses/',AllResponses.as_view(),name='all-responses'),
    path('api/responses/<int:pk>',SingleResponses,name='single-response'),
]