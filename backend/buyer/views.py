from rest_framework import viewsets, status
from rest_framework.response import Response
from merchant.models import Payment
from .serializers import PaymentSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.conf import settings
from datetime import datetime
from drf_spectacular.utils import extend_schema

class PaymentGatewayViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    @extend_schema(responses=PaymentSerializer)
    def retrieve_payment_details(self, request, pk=None):
        try:
            payment_instance = Payment.objects.select_related('merchant').get(pk=pk)
            serializer = PaymentSerializer(payment_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(responses=PaymentSerializer)
    def complete_payment(self, request, pk=None):
        print('complete_payment',request.data,pk)
        payment_instance_authorization_done = True
        try:
            payment_instance = Payment.objects.get(pk=pk)
            buyer_id = request.data.get('buyer_id')

            if payment_instance.status == 'completed':
                return Response({'message': 'Payment has already been completed'}, status=status.HTTP_200_OK)
            
            if not payment_instance_authorization_done:
                return Response({'error': 'Payment not authorized'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = PaymentSerializer(payment_instance, data={'buyer': buyer_id, 'status': 'completed', 'paid_at': datetime.now()}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Payment completed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

class PaymentRefundViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def refund(self, request, pk=None):
        payment_found= True

        try:
            if payment_found:
            
                return Response({'message': 'Refund initiated successfully'}, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
