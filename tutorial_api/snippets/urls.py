from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename='user')

urlpatterns = [
    path('', include(router.urls)),
]