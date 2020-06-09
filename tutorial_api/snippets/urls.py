from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include
from snippets import views

router = SimpleRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippets')

urlpatterns = [
    path('', include(router.urls)),
]