from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from drf_spectacular.utils import extend_schema


class SongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_id = self.kwargs.get("pk")
        return Song.objects.filter(album_id=album_id)

    def perform_create(self, serializer):
        album_id = self.kwargs.get("pk")
        album = get_object_or_404(Album, pk=album_id)
        serializer.save(album=album)

    @extend_schema(operation_id="get_songs", description="Rota de listagem de songs", summary="Listar songs")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(operation_id="post_songs", description="Rota de criação de song", summary="Criar song")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
