from django.urls import path, include
from .views import ShowNotesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'notes', ShowNotesViewSet)



urlpatterns = [
   path('', include( router.urls))
]