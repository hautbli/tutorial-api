from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from snippets import views
from rest_framework.authtoken import views
from snippets.views import SnippetViewSet, CustomAuthToken

router = SimpleRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api-token-auth/', CustomAuthToken.as_view())
]