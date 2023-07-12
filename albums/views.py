from .models import Album
from .serializers import AlbumSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema


class AlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(operation_id="get_albums", description="Rota de listagem de albums", summary="Listar albums")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(operation_id="post_albums", description="Rota de criação de album", summary="Criar album")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
