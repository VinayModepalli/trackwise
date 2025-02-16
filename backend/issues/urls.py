from django.urls import path, include

from issues.views import hello, IssueAPIView, CommentAPIView

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('issue/<int:pk>', IssueAPIView.as_view(), name='tasks-get-put'),
    path('issue/', IssueAPIView.as_view(),  name='tasks'),
    path('comment/<int:pk>', CommentAPIView.as_view(), name='comments-get-put'),
    path('comment/', CommentAPIView.as_view(),  name='comments'),
]