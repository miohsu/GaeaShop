from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name='购买数量')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s(%d)'.format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("PAYING", "待支付"),
    )
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=32, unique=True, verbose_name='订单编号')
    trade_no = models.CharField(max_length=64, null=True, blank=True, unique=True, verbose_name='交易号')
    pay_status = models.CharField(max_length=32, choices=ORDER_STATUS, default='PAYING', verbose_name='订单状态')
    post_script = models.CharField(max_length=128, verbose_name='订单留言')
    order_mount = models.FloatField(default=0.0, verbose_name='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    address = models.CharField(max_length=128, default='', verbose_name='收货地址')
    signer_name = models.CharField(max_length=32, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=32, verbose_name='联系电话')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name='订单信息', related_name='goods', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
