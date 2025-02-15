from django.urls import path, include

from issues.views import hello, IssueAPIView

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('issue/<int:pk>', IssueAPIView.as_view(), name='tasks-get-put'),
    path('issue/', IssueAPIView.as_view(),  name='tasks')
]