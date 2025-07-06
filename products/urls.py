from django.urls import path,include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, index


router = DefaultRouter()
router.register(r'products',ProductViewSet)

urlpatterns=[
    path('',index),
    path('',include(router.urls)),
]