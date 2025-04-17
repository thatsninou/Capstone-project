from django.urls import path
from .views import bookingview, menuview

urlpatterns = [
    path('booking/', bookingview.as_view()),
    path('menu/', menuview.as_view()),
]
