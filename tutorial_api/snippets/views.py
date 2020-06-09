from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, filters
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', ]

# class SnippetViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
#     def retrieve(self, request, pk=None):
#         queryset = Snippet.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = SnippetSerializer(user)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         serializer = SnippetSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def update(self, request, pk=None):
#         instance = Snippet.objects.get(pk=pk)
#         serializer = SnippetSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     def destroy(self, request, pk=None):
#         instance = Snippet.objects.get(pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
