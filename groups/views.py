from rest_framework.views import APIView, Request, Response, status
from .models import Group
from .serializers import GroupSerializer

class GroupView(APIView):
    def get(self, req: Request) -> Response:
        groups = Group.objects.all()

        serializer = GroupSerializer(instance=groups,many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK )
        
    def post(self, req: Request) -> Response:
        serializer = GroupSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
        
        group = Group.objects.create(**serializer.validated_data)

        serializer = GroupSerializer(instance=group)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
