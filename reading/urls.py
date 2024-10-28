from django.urls import path
from .api import TestListAPIView, TestDetailAPIView, TestCreateAPIView
from . import views
from .api2 import SubmitScoreView

urlpatterns = [
    path('api/tests/', TestListAPIView.as_view(), name='test_list_api'),
    path('api/tests/<int:test_id>/submit_score/', SubmitScoreView.as_view(), name='submit_score'),
    path('api/tests/create/', TestCreateAPIView.as_view(), name='test_create_api'),
    path('api/tests/<int:pk>/', TestDetailAPIView.as_view(), name='test_detail_api'),
    path("", views.index, name="index"),
    path("<int:page_id>/page", views.page, name="page"),
    path('test/<int:test_id>/', views.question_detail, name='question_detail_default'),
    path('test/<int:test_id>/question/<int:question_id>/', views.question_detail, name='question_detail'),
]