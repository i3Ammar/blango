from rest_framework import serializers

from blango_auth.models import User
from blog.models import Post, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field = 'value',
        many = True,
        queryset = Tag.objects.all()
    )
    author = serializers.HyperlinkedRelatedField(
        queryset = User.objects.all(),
        view_name = "api_user_detail",
        lookup_field = "email",
    )

    class Meta:
        model = Post
        fields = "__all__"
        readonly = ['modified_at', 'created_at']
