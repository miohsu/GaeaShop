from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class GoodsCategory(models.Model):
    '''
    商品分类
    '''
    CATEGORY_TYPE = (
        (1, '一级类别'),
        (2, '二级类别'),
        (3, '三级类别'),
    )
    name = models.CharField(max_length=64, null=True, blank=True, verbose_name='类别名', help_text='类别名')
    code = models.CharField(max_length=32, null=True, blank=True, verbose_name='类别code', help_text='类别code')
    desc = models.TextField(max_length=128, null=True, blank=True, verbose_name='类别描述')
    category_type = models.CharField(max_length=32, choices=CATEGORY_TYPE, verbose_name='类别级别', help_text='类别级别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父类别', help_text='父类别',
                                        related_name='sub_cat', on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = '商品类别'

        def __str__(self):
            return self.name


class GoodsCategoryBrand(models.Model):
    '''
    品牌名
    '''
    category = models.ForeignKey(GoodsCategory, related_name='brand', verbose_name='商品类别', on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=32, verbose_name='品牌名', help_text='品牌名')
    desc = models.TextField(max_length=128, null=True, blank=True, verbose_name='品牌描述', help_text='品牌描述')
    image = models.ImageField(upload_to='brands/')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'

        def __str__(self):
            return self.name


class Goods(models.Model):
    '''
    商品
    '''
    category = models.ForeignKey(GoodsCategory, related_name='goods', verbose_name='商品类别', on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=32, null=True, blank=True, verbose_name='商品SN号')
    name = models.CharField(max_length=100, verbose_name='商品名')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    sold_num = models.IntegerField(default=0, verbose_name='销售量')
    fav_num = models.IntegerField(default=0, verbose_name='收藏数')
    goods_num = models.IntegerField(default=0, verbose_name='库存')
    market_price = models.FloatField(default=0, verbose_name='市场价')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.TextField(max_length=500, verbose_name='商品简短描述')
    goods_desc = UEditorField(verbose_name='内容', imagePath='goods/images/', width=1000, height=300,
                              filePath='goods/files/', default='')
    ship_free = models.BooleanField(default=False, verbose_name='是否承担运费')
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

        def __str__(self):
            return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name='商品类目', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页商品类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    '''
    商品轮播图
    '''
    goods = models.ForeignKey(Goods, verbose_name='商品', related_name='image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', verbose_name='图片', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.goods.name


class Banner(models.Model):
    '''
    轮播商品
    '''
    goods = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner/', verbose_name='轮播图片')
    index = models.SmallIntegerField(default=0, verbose_name='轮播顺序')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.goods.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(max_length=32, default='', verbose_name='热搜词')
    index = models.IntegerField(default=0, verbose_name='排序')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
