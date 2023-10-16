from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson, Payment, Subscription
from education.validators import LinkValidator


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    is_subscribed = SubscriptionSerializer(source='subs', many=True,
                                           read_only=True)

    def get_lesson_count(self, instance):
        if instance.course.all():
            return instance.course.all().count()
        else:
            return 0

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lessons = SerializerMethodField()

    def get_course_lessons(self, instance):
        return [lesson.title for lesson in
                Lesson.objects.filter(course=instance)]

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'



