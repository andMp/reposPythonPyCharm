from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZavdViewSet, index

router=DefaultRouter()
router.register(r'my_spis_zavd',ZavdViewSet)

urlpatterns=[
    path('',index),
    path('api/',include(router.urls)),
]