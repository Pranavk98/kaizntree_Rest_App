from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from .filters import ItemFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.dateparse import parse_date



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter

    def get_queryset(self):
        queryset = Item.objects.all()
        stock_status = self.request.query_params.get('stock_status')
        created_at = self.request.query_params.get('created_at')

        if stock_status is not None:
            queryset = queryset.filter(stock_status=stock_status)

        if created_at is not None:
            created_at_date = parse_date(created_at)
            if created_at_date:
                queryset = queryset.filter(created_at=created_at_date)
            else:
                
                pass

        return queryset