from rest_framework import serializers
from .models import Announce, Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    announce = serializers.ReadOnlyField(source='announce.title')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'announce'] 
        # ref_name = 'announces_comments' # mandatory for drf_yasg


class AnnounceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Announce
        fields = ['id', 'title', 'body', 'owner', 'comments'] 
        # ref_name = 'announces_announces' # mandatory for drf_yasg

