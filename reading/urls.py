from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:page_id>/page", views.page, name="page"),
    path('test/<int:test_id>/', views.question_detail, name='question_detail_default'),
    path('test/<int:test_id>/question/<int:question_id>/', views.question_detail, name='question_detail'),
]