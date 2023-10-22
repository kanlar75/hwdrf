from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from education.models import Course, Lesson, Payment, Subscription
from education.services.create_pay import create_session
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
    # count_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True, read_only=True)
    subscribed_users = SubscriptionSerializer(source='subscriptions',
                                              many=True,
                                              read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    def get_payment_url(self, payment):
        return create_session(payment)

    class Meta:
        model = Payment
        fields = '__all__'

