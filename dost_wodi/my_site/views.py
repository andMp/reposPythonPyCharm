from django.shortcuts import render
from rest_framework import viewsets
from .models import Zamovl
from .serializations import ZamovlSerializer
# Create your views here.
class ZamovlViewSet(viewsets.ModelViewSet):
    queryset = Zamovl.objects.all()
    serializer_class = ZamovlSerializer

def index(request):
    return render(request,'main/index.html')