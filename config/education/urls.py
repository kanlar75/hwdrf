from rest_framework.routers import DefaultRouter
from django.urls import path

from education.apps import EducationConfig
from education.views import CourseViewSet, LessonCreateAPIView, \
    LessonListAPIView, LessonRetriveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentListAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = ([
                   path('lesson/create/', LessonCreateAPIView.as_view(),
                        name='lesson_create'),
                   path('lesson/', LessonListAPIView.as_view(),
                        name='lesson_list'),
                   path('lesson/<int:pk>/', LessonRetriveAPIView.as_view(),
                        name='lesson_detail'),
                   path('lesson/update/<int:pk>/',
                        LessonUpdateAPIView.as_view(), name='lesson_update'),
                   path('lesson/delete/<int:pk>/',
                        LessonDestroyAPIView.as_view(), name='lesson_delete'),

                   path('payments/', PaymentListAPIView.as_view(),
                        name='payment_list')

               ] + router.urls)
