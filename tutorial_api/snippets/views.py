from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, filters
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters import rest_framework as filters1, CharFilter


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class SnippetFilter(filters1.FilterSet):
    min_price = filters1.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters1.NumberFilter(field_name="price", lookup_expr='lte')

    # code_code = CharFilter(field_name='code', method='filter_code')

    starts_with_title = CharFilter(field_name="code", method="filter_startswith_code")

    def filter_startswith_code(self, queryset, name, value):
        code_filter = {f'{name}__startswith': value}
        print(code_filter)
        return queryset.filter(**code_filter)

    class Meta:
        model = Snippet
        fields = ['price',]


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['code', ]

    filter_backends = (filters1.DjangoFilterBackend,)
    filterset_class = SnippetFilter

    # 토큰 체크
    def list(self, request, *args, **kwargs):
        print(request.user.username)
        return super().list(request, *args, **kwargs)

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
