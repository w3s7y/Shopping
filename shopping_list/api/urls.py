from django.urls import path, include
from rest_framework import routers, viewsets, serializers
from django.contrib.auth.models import User
import api.models


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api.models.List
        fields = ('id', 'name', 'owner')


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api.models.Shop
        fields = ('id', 'name', 'address', 'website')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api.models.Item
        fields = ('id', 'name', 'description', 'price', 'price_unit', 'barcode')


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api.models.Offer
        fields = ('id', 'shop', 'item', 'price', 'price_unit', 'end_date')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = api.models.Favorite
        fields = ('id', 'owner', 'item')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = api.models.List.objects.all()
    serializer_class = ListSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = api.models.Shop.objects.all()
    serializer_class = ShopSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = api.models.Item.objects.all()
    serializer_class = ItemSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = api.models.Offer.objects.all()
    serializer_class = OfferSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = api.models.Favorite.objects.all()
    serializer_class = FavoriteSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'lists', ListViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'items', ItemViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'favorites', FavoriteViewSet)


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
