from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Recipe
from .serializer import RecipeSerializer

# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            return Response({
                'message': "Recipe successfully created!",
                "recipe": [serializer.data]
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': "Recipe creation failed!",
            "recipe": "title, making_time, serves, ingredients, cost"
        }, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"recipe": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'message': "Recipe details by id",
                "recipe": [serializer.data]
            }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "No Recipe found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response({
                "message": "Recipe successfully updated!",
                "recipe": [serializer.data]
            }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "No Recipe found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Recipe successfully removed!"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "No Recipe found"}, status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()


def topview(request):
    return Response(status=status.HTTP_404_NOT_FOUND)
