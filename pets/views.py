from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class PetView(APIView, PageNumberPagination):
    def get(self, req: Request) -> Response:
        
        trait = req.query_params.get("trait", None)
        
        if trait:
            pets=Pet.objects.filter(
                traits__name__iexact=trait
            )
        else:
            pets = Pet.objects.all()
            
        result_page = self.paginate_queryset(pets, req)
        serializer = PetSerializer(instance=result_page, many=True)
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)
       
        group = serializer.validated_data.pop("group")

        traits = serializer.validated_data.pop("traits")

        group_obj = Group.objects.filter(
            scientific_name__iexact=group["scientific_name"]
        ).first()

        if not group_obj:
            group_obj = Group.objects.create(**group)

        pet = Pet.objects.create(**serializer.validated_data, group=group_obj)
        
        for trait_dict in traits:
            trait_obj = Trait.objects.filter(
                name__iexact=trait_dict["name"]
            ).first()

            if not trait_obj:
                trait_obj = Trait.objects.create(**trait_dict)

            pet.traits.add(trait_obj)
        
        serializer = PetSerializer(instance=pet)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, req: Request, pet_id:int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        serializer =  PetSerializer(instance=pet)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, req: Request, pet_id:int) -> Response:
        serializer = PetSerializer(data=req.data, partial=True)
        
        pet = get_object_or_404(Pet, id=pet_id)
        
        serializer.is_valid(raise_exception=True)
        
        group = serializer.validated_data.pop("group", None)

        traits = serializer.validated_data.pop("traits", None)
        
        for key, value, in serializer.validated_data.items():
            setattr(pet, key, value)
        
        if not group == None:
            group_obj = Group.objects.filter(
                scientific_name__iexact=group["scientific_name"]
            ).first()

            if not group_obj:
                group_obj = Group.objects.create(**group)

            pet.group=group_obj

        if not traits == None:
            pet.traits.clear()
            for trait_dict in traits:
                trait_obj = Trait.objects.filter(
                    name__iexact=trait_dict["name"]
                ).first()

                if not trait_obj:
                    trait_obj = Trait.objects.create(**trait_dict)

                pet.traits.add(trait_obj)

        serializer = PetSerializer(instance=pet)
        pet.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete (self, req: Request, pet_id:int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)

        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        

       