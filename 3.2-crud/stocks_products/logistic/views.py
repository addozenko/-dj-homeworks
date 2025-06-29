from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # количество объектов на странице
    page_size_query_param = 'page_size'  # параметр запроса для клиента
    max_page_size = 100  


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description'] 
    pagination_class = StandardResultsSetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['address']
    search_fields = ['address']  
    pagination_class = StandardResultsSetPagination