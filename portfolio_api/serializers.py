from rest_framework import serializers
from portfolio.models import Projects, Category, Feedback
from taggit.serializers import TagListSerializerField
from taggit.models import Tag


class ProjectsSerializer(serializers.ModelSerializer):
    cat = serializers.SlugRelatedField(slug_field='name', read_only=True)
    tags = TagListSerializerField()
    project_stage = serializers.CharField(source='get_project_stage_display', read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'
