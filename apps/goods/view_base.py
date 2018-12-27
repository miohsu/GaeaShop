from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

from goods.models import Goods


class GoodsListView(View):

    def get(self, request):
        """
        通过django View 实现商品列表
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
