from rest_framework import viewsets
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from rest_framework.exceptions import NotFound


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    





class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(f'inventory_item_{item_id}')
        if cached_item:
            return Response(cached_item)

        item = self.get_object()
        serializer = self.get_serializer(item)
        cache.set(f'inventory_item_{item_id}', serializer.data, timeout=3600)
        return Response(serializer.data)




def get_object(self):
    try:
        return InventoryItem.objects.get(pk=self.kwargs['pk'])
    except InventoryItem.DoesNotExist:
        raise NotFound('Item not found')