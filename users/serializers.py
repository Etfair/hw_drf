from datetime import date

from rest_framework import serializers
from users.models import User, Subscription


class UserSerializer(serializers.ModelSerializer):
    user_payment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'user_payment_count')

    def get_user_payment_count(self, instance):
        return instance.payment_set.all().count()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class MyTokenObtainPairSerializer(serializers.ModelSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        user.last_login = date.today()
        user.save()

        return token
