from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import ExtraFood
from .serializers import ExtraFoodSerializer
from registration_and_login.models import Provider


class IsProviderOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user
            and request.user.is_authenticated
            and hasattr(request.user, 'provider')
            and obj.provider.user == request.user
        )


class ExtraFoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExtraFood.objects.all()
    serializer_class = ExtraFoodSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        try:
            provider = user.provider
        except Provider.DoesNotExist:
            raise PermissionDenied('Only authenticated providers can create extra food entries.')
        serializer.save(provider=provider)


class ExtraFoodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraFood.objects.all()
    serializer_class = ExtraFoodSerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsProviderOwner()]

    def check_object_permissions(self, request, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return
        super().check_object_permissions(request, obj)
