from rest_framework import serializers
from .models import Issue, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['created_at', 'modified_at']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ['created_at', 'modified_at']
    
    def validate_status(self, value):
        choices = [i[0] for i in Issue.STATUS_CHOICES]
        if value not in choices:
            raise serializers.ValidationError("Invalid Status")
        return value

