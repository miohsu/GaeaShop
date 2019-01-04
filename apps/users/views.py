import random

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from utils.SendMsg import SendMsg
from GaeaShop.settings import API_KEY
from apps.users.models import VerifyCode
from users.serializers import MsgSerilizer

# Create your views here.
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class MsgCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = MsgSerilizer

    def generate_code(self, count):
        """
        生成数字验证码
        :param count:
        :return:
        """
        seeds = '1234567890'
        return ''.join([random.choice(seeds) for i in range(count)])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data['mobile']
        code = self.generate_code(4)
        send_msg = SendMsg(API_KEY)
        msg_status = send_msg.send_msg(code, mobile)
        if msg_status['code'] != 0:
            return Response({
                'mobile': msg_status['msg'],
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile,
            }, status=status.HTTP_201_CREATED)
