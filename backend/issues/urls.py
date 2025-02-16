from django.urls import path, include

from issues.views import hello, IssueListCreateAPIView, IssueDetailUpdateDeleteAPIView, CommentListCreateAPIView, CommmentDetailUpdateDeleteAPIView

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('issue/<int:pk>/', IssueDetailUpdateDeleteAPIView.as_view(), name='tasks-get-put'),
    path('issue/', IssueListCreateAPIView.as_view(),  name='tasks'),
    path('comment/<int:pk>/', CommmentDetailUpdateDeleteAPIView.as_view(), name='comments-get-put'),
    path('comment/', CommentListCreateAPIView.as_view(),  name='comments'),
]