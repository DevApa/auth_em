from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from entrepreneur.models import Usuario
from authentication.serializers import UserListSerializers, UserSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    # lista los usuarios activos ingresados al sistemna
    if request.method == 'GET':
        users = Usuario.objects.filter(is_active=True).values('id', 'username', 'email', 'password', 'first_name')
        user_serializer = UserListSerializers(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        """
            Habilita la creación de usuarios solicitando 
        """
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    user = Usuario.objects.filter(id=pk).first()

    # Retrieve
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            user.is_active = False
            user.save()
            return Response({'message': 'Usuario eliminado correctamente!'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'Sin datos para la consulta, favor corregir y reintentar!'},
                    status=status.HTTP_400_BAD_REQUEST)
