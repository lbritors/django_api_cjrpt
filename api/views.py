from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer
from rest_framework.exceptions import PermissionDenied


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token_data = serializer.save()
            return Response(token_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action in ['create', 'retrieve', 'list']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.id != request.user.id:
            raise PermissionDenied("You dont't have permission to alter data from another user.")

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.id != request.user.id:
            raise PermissionDenied("You dont't have permission to destroy data from another user.")

        return super().destroy(request, *args, **kwargs)