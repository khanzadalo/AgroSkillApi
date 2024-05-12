from rest_framework import serializers
from .models import Product, Category, CartItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'url', "name", "slug", "category", "price", "discount",
            "image", "description")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'image',
            'is_staff', 'is_active', 'is_superuser')

    image = serializers.ImageField(source='profile.image', required=False)


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'product')


class CartItemAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ('quantity', 'product_id')
        extra_kwargs = {
            'quantity': {'required': True},
            'product_id': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        product = get_object_or_404(Product, id=validated_data['product_id'])
        if product.quantity == 0 or product.is_available is False:
            raise serializers.ValidationsError(
                {'not available': 'the product is not available.'})

        cart_item = CartItem.objects.create(
            product=product,
            user=user,
            quantity=validated_data['quantity']
            )
        cart_item.save()
        cart_item.add_amount()
        product.quantity = product.quantity - cart_item.quantity
        product.save()
        return cart_item