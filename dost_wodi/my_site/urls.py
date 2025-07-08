from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ZamovlViewSet, index
from ..dost_wodi.urls import urlpatterns

router = DefaultRouter()
router.register(r'my_site',ZamovlViewSet)

urlpatterns=[
    path('',index),
    path('api/',include(router.urls)),
]
