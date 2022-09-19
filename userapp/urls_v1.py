from django.urls import path

from userapp.views import AppUserCustomViewSet

urlpatterns = [
    path('api/<str:version>/users/', AppUserCustomViewSet.as_view({'get': 'list'})),
]