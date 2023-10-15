from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from .models import Course, Lesson, Payment
from .permissions import IsOwner, IsModerator
from .serializers import CourseSerializer, LessonSerializer, \
    CourseDetailSerializer, PaymentSerializer
from users.models import UserRoles


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseSerializer,
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.default_serializer)

    def get_queryset(self):
        if (self.request.user.is_superuser or self.request.user.is_staff
                or self.request.user.role == UserRoles.MODERATOR):
            return Course.objects.all()

        return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        if self.request.method in ['CREATE', 'DELETE']:
            self.permission_classes = [IsOwner, ~IsModerator]
        else:
            self.permission_classes = [IsOwner, ]
        return super(CourseViewSet, self).get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_method')
    ordering_fields = ('date_of_payment',)
