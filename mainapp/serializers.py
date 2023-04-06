

from .models import Shop, User
from rest_framework import serializers

# Create a class that links student details with the serializer
# serializer -> convert data to json string


class SerializeShop(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'latitude', 'longitude', 'address')
class SerializeUser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'latitude', 'longitude', 'distance')