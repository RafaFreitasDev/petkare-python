from rest_framework.views import APIView, Request, Response, status
from .models import Trait
from .serializers import TraitSerializer

class TraitView(APIView):
    def get(self, req: Request) -> Response:
        traits = Trait.objects.all()

        serializer = TraitSerializer(instance=traits,many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = TraitSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
            
        trait = Trait.objects.create(**serializer.validated_data)

        serializer = TraitSerializer(instance=trait)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
