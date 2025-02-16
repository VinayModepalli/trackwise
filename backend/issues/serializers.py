from rest_framework import serializers
from .models import Issue, Comment

# In ModelSerializers, we can customize the creation, updation, deletion etc via following methods:
# create(), update()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['created_at', 'modified_at']

class IssueSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Issue
        fields = ['id', 'summary', 'description', 'due_date', 'status', 'comments'] #  'created_at', 'modified_at'
        read_only_fields = ['id', 'created_at', 'modified_at']
    
    def validate_status(self, value):
        choices = [i[0] for i in Issue.STATUS_CHOICES]
        if value not in choices:
            raise serializers.ValidationError("Invalid Status")
        return value

