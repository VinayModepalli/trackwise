from rest_framework import serializers
from .models import Issue, Comment

# In ModelSerializers, we can customize the creation, updation, deletion etc via following methods:
# create(), update()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'modified_at', 'created_by']

class IssueSerializer(serializers.ModelSerializer):
    # Get all the comments linked to the current Issue and use it as a field
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'summary', 'description', 'due_date', 'status', 'comments', 'created_by', 'assignee'] #  'created_at', 'modified_at'
        read_only_fields = ['id', 'created_at', 'modified_at', 'created_by']
    
    def validate_status(self, value):
        choices = [i[0] for i in Issue.STATUS_CHOICES]
        if value not in choices:
            raise serializers.ValidationError("Invalid Status")
        
        disallowed_transitions = {
            'OPEN': ['UNDER_REVIEW', 'DONE'],
            'BLOCKED': ['DONE']
        }

        if self.instance.status in disallowed_transitions and value in disallowed_transitions[self.instance.status]:
            raise serializers.ValidationError(f"Cannot move the status from {self.instance.status} to {value}")

        return value

