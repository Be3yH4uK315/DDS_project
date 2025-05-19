from rest_framework import viewsets
from .models import Status, Type, Category, Subcategory, DDSRecord
from .serializers import *
from .filters import DDSRecordFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в сервис управления ДДС!</h1>")

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class DDSRecordViewSet(viewsets.ModelViewSet):
    queryset = DDSRecord.objects.all()
    serializer_class = DDSRecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DDSRecordFilter