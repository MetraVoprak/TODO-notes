from django.urls import path

from userapp.views import AppUserCustomViewSet

app_name = 'userapp'
urlpatterns = [
    path('', AppUserCustomViewSet.as_view({'get': 'list'})),
]