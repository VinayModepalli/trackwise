from django.db import models
from users.models import User

# Create your models here.
# class Project(models.Model):
#     pass

class Issue(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('BLOCKED', 'Blocked'),
        ('UNDER_REVIEW', 'Under Review'),
        ('DONE', 'Done'),
    )
    # id = models.CharField()
    summary = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=False, blank=False, default='OPEN')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned', blank=True, null=True)
    # Add a project here

    created_by = models.ForeignKey(User, related_name='issue_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary

class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='comment_created', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    pass
