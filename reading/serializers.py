from rest_framework import serializers
from .models import Test, Passage,Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)  # Nesting choices inside question

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class PassageSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)  # Nesting questions inside passage

    class Meta:
        model = Passage
        fields = ['id', 'content', 'questions']

class TestSerializer(serializers.ModelSerializer):
    passages = PassageSerializer(many=True)  # Nesting passages inside test

    class Meta:
        model = Test
        fields = ['id', 'title', 'description']
