# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test, TestScore
from .serializers import TestScoreSerializer

class SubmitScoreView(APIView):
    def post(self, request, test_id):
        user_name = request.data.get('user_name')
        score = request.data.get('score')

        try:
            test = Test.objects.get(id=test_id)
            test_score = TestScore.objects.create(test=test, user_name=user_name, score=score)
            serializer = TestScoreSerializer(test_score)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Test.DoesNotExist:
            return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)
