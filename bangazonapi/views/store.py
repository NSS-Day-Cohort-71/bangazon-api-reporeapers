from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from bangazonapi.models import Store
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.contrib.auth.models import User



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class StoreSerializer(serializers.ModelSerializer):

    seller = SellerSerializer()

    class Meta:
        model = Store
        fields = ('id', 'seller', 'name', 'description')
    

class Stores(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context={'request': request})
        return Response(serializer.data)
