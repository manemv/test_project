from rest_framework import generics
from .models import Test
from .serializers import TestSerializer

# View to get all tests with their related passages, questions, and choices
class TestListAPIView(generics.ListAPIView):
    queryset = Test.objects.prefetch_related('passages__questions__choices')
    serializer_class = TestSerializer

# View to get a specific test with related data
class TestDetailAPIView(generics.RetrieveAPIView):
    queryset = Test.objects.prefetch_related('passages__questions__choices')
    serializer_class = TestSerializer
