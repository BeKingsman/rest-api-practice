from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Snippet

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class modelserial(serializers.ModelSerializer):
#     allsnippets = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='snippets-detail'
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'groups','allsnippets']


class SnippetSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class modelserial(serializers.ModelSerializer):
    allsnippets = SnippetSerializer(
        many=True,
        read_only=True,

    )

    class Meta:
        model = User
        fields = ['username', 'email', 'groups','allsnippets']
#


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
