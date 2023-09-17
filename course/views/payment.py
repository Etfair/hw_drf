from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from course.models import Payment
from course.paginators import ListPaginator
from course.seriallizers.payment import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['method']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
