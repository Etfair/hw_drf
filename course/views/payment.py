from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Payment
from course.paginators import ListPaginator
from course.seriallizers.payment import PaymentSerializer, PaymentCreateSerializer, PaymentRetrieveSerializer
from course.service import get_create_payment, get_payment_retrieve


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['method']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.validated_data.get('lesson')
        course = serializer.validated_data.get('course')
        if not lesson and not course:
            raise serializers.ValidationError({
                'non_empty_fields': 'Заполните необходимые поля'
            })
        new_mat = serializer.save()
        new_mat.user = self.request.user
        new_mat.session = get_create_payment(new_mat).id
        new_mat.save()


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentRetrieveSerializer
    queryset = Payment.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        session = get_payment_retrieve(obj.session)
        if session.payment_status == 'paid' and session.status == 'complete':
            obj.is_paid = True
            obj.save()
        self.check_object_permissions(self.request, obj)
        return obj
