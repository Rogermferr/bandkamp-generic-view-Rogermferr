from rest_framework import generics
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from drf_spectacular.utils import extend_schema


class UserView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(operation_id="post_user", description="Rota de criação de usuário", summary="Criar usuário")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @extend_schema(operation_id="list_user", description="Rota de listagem de usuários", summary="Listar usuário")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    @extend_schema(
        operation_id="retrieve_user",
        description="Rota de recuperar dados do usuário logado",
        summary="Listar dados de usuário logado",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(operation_id="user_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(operation_id="update_user", description="Rota de atualizar usuário", summary="Atualizar usuário")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(operation_id="delete_user", description="Rota de deletar usuário", summary="Deletar usuário")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
