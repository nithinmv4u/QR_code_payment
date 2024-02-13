from django.urls import path
from .views import PaymentGatewayViewSet, PaymentRefundViewSet

app_name = 'buyer'

urlpatterns = [
    path('payment-gateway/<int:pk>/', PaymentGatewayViewSet.as_view({
        'get': 'retrieve_payment_details',
        'put': 'complete_payment'
    }), name='payment_gateway'),
    path('payment-refund/<int:pk>/', PaymentRefundViewSet.as_view({
        'put': 'refund'
    }), name='payment_refund'),
]