from rest_framework import serializers

from goods.models import Goods
from goods.models import GoodsCategory


class GoodsCategorySerializer3(serializers.ModelSerializer):
    """
    三级商品类别序列化
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsCategorySerializer2(serializers.ModelSerializer):
    """
    二级商品类别序列化
    """
    sub_cat = GoodsCategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
    一级商品类别序列化
    """
    sub_cat = GoodsCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品数据序列化
    """
    category = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
