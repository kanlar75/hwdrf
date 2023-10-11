from rest_framework.viewsets import ModelViewSet, generics
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from education.models import Course, Lesson, Payment
from education.serializers import CourseSerializer, LessonSerializer, \
    CourseDetailSerializer, PaymentSerializer


class CourseViewSet(ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    serializer_classes = {
        "retrieve": CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    serializer_classes = {
        "retrieve": CourseDetailSerializer
    }


class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'method')
    ordering_fields = ('payment_date',)
