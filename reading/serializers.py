from rest_framework import serializers
from .models import Test, Passage, Paragraph, Question, Choice, TestScore

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)  # Nesting choices inside question

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'paragraph']

class PassageSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)  # Nesting questions inside passage
    paragraphs = ParagraphSerializer(many=True)
    class Meta:
        model = Passage
        fields = ['id','title', 'description','paragraphs', 'questions']

class TestSerializer(serializers.ModelSerializer):
    passages = PassageSerializer(many=True)  # Nesting passages inside test

    class Meta:
        model = Test
        fields = ['id', 'title', 'description', 'passages']

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = ['test', 'user_name', 'score', 'completed_at']