from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Merchant
from io import BytesIO
import qrcode
from .serializers import MerchantPaymentSerializer, QRCodeSerializer
import base64
from rest_framework.permissions import AllowAny
from urllib.parse import urlencode
from django.db import transaction
from drf_spectacular.utils import extend_schema

class QRCodeViewSet(ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(responses=MerchantPaymentSerializer)
    def create(self, request):
        payment_serializer = MerchantPaymentSerializer(data=request.data)
        payment_serializer.is_valid(raise_exception=True)

        merchant_id = request.data.get('merchant')
        try:
            merchant_instance = Merchant.objects.get(pk=merchant_id)
        except Merchant.DoesNotExist:
            return Response({'error': 'Merchant not found'}, status=status.HTTP_404_NOT_FOUND)
        with transaction.atomic():
            payment_instance = payment_serializer.save(merchant=merchant_instance)

            amount = payment_instance.amount
            description = payment_instance.description
            payment_id = payment_instance.id

            frontend_base_url = 'http://localhost:8080/buyer'
            frontend_url_params = urlencode({'payment_id': payment_id})
            payment_url = f"{frontend_base_url}?{frontend_url_params}"

            qr_code_content = f"Click to pay: {payment_url}"

            qr_code_img = qrcode.make(qr_code_content)
            qr_code_img_pil = qr_code_img.get_image()
            buffer = BytesIO()
            qr_code_img_pil.save(buffer, format='PNG')
            qr_code_img_bytes = buffer.getvalue()

            qr_code_img_base64 = base64.b64encode(qr_code_img_bytes).decode('utf-8')

            qr_code_data = {
                'qr_code_img': qr_code_img_base64,
                'payment_url': payment_url,
                'merchant': merchant_instance.pk  
            }
            qr_code_serializer = QRCodeSerializer(data=qr_code_data)
            if qr_code_serializer.is_valid():
                qr_code_instance = qr_code_serializer.save()
            else:
                return Response(qr_code_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'qr_code_img': qr_code_img_base64, 'payment_url': payment_url}, status=status.HTTP_200_OK)

