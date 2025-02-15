from django.urls import path, include

from issues.views import hello

urlpatterns = [
    path('hello/', hello, name='hello')
]