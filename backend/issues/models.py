from django.db import models

# Create your models here.
# class Project(models.Model):
#     pass

class Issue(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('UNDER_REVIEW', 'Under Review'),
        ('DONE', 'Done'),
    )
    # id = models.CharField()
    summary = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=False, blank=False, default='OPEN')
    # Add a project here

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def set_status(self, new_status):
        if new_status not in Issue.STATUS_CHOICES:
            raise ValueError(f"Invalid status: {new_status}")
        disallowed_transitions = {
            'OPEN': ['UNDER_REVIEW', 'DONE'],

        }
        if self.status in disallowed_transitions and new_status in disallowed_transitions[self.status]:
            raise ValueError(f"Cannot move the status from {self.status} to {new_status}")

        self.status = new_status
        self.save()
        return self.status

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    pass
