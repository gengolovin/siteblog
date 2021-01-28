from django.urls import path, include
from .views import SubscriptionView

urlpatterns = [
    path('', SubscriptionView.as_view(), name='subscription'),
]
