from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_user(request, format=None):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)
