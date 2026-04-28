from django.urls import path

from .views import ExtraFoodListCreateAPIView, ExtraFoodRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ExtraFoodListCreateAPIView.as_view(), name='extrafood-list-create'),
    path('<int:pk>/', ExtraFoodRetrieveUpdateDestroyAPIView.as_view(), name='extrafood-detail'),
]
