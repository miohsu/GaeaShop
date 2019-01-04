import re
from datetime import datetime
from datetime import timedelta

from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import VerifyCode

from GaeaShop.settings import REGEX_MOBILE

User = get_user_model()


class MsgSerilizer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile:
        :return:
        """
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已存在')

        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('非法手机号码')

        one_mintes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(create_time__gt=one_mintes_age, mobile=mobile).count():
            raise serializers.ValidationError('发送太频繁')

        return mobile
