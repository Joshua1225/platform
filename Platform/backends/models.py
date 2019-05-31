from django.db import models
from django.utils import timezone
# Create your models here.

# ImageField 和 FileField 都有up_load参数控制上传文件的位置， 目前没填

class Users(models.Model):
    """用户  含专家"""
    user_id = models.CharField(max_length=21, primary_key=True, db_index=True)
    password = models.CharField(max_length=21)
    user_name = models.CharField(max_length=21)
    credit = models.IntegerField(default=0)
    interest = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    avator = models.ImageField()     # 这里有两个可选参数规定图片显示大长和宽，根据前端页面需要定
    signature = models.TextField(null=True)
    type = models.IntegerField(default=0, choices=((0, u"普通用户"), (1, u"专家")))
    institute = models.CharField(max_length=255, null=True)
    field = models.TextField(null=True)
    experience = models.TextField(null=True)
    education = models.TextField(null=True)
    tendency = models.TextField(null=True)


class Administrators(models.Model):
    """管理员"""
    admin_id = models.CharField(max_length=21, primary_key=True)
    password = models.CharField(max_length=21)


class Papers(models.Model):
    """论文"""
    id = models.UUIDField(primary_key=True, db_index=True)
    title = models.CharField(max_length=255)
    authors_name = models.CharField(max_length=255)
    authors_institute = models.CharField(max_length=255, null=True)
    venue = models.CharField(max_length=255, null=True)         # 论文出处
    year = models.IntegerField(null=True)
    keywords = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, null=True)
    n_citation = models.IntegerField(default=0)
    references = models.CharField(max_length=65535)
    # page_stat
    # page_end
    doc_type = models.CharField(max_length=255)
    lang = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=True)
    # volumn
    # issue
    issn = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=255, null=True)
    # doi
    pdf = models.URLField()
    url = models.URLField()
    abstract = models.TextField()
    belonging = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)


class Trades(models.Model):
    """交易记录"""
    price = models.IntegerField(default=0)
    buyer_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Papers, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)


class Messages(models.Model):
    """站内信"""
    type = models.IntegerField(choices=((1, "上传论文认证"), (2, "身份认证"), (3, "论文归属权申诉")))
    content = models.TextField()
    reply = models.TextField
    time = models.TimeField(auto_now_add=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    file = models.FileField()
    object_id = models.CharField(max_length=255)
    state = models.IntegerField(choices=((0, "未处理"), (1, "肯定"), (2, "否定")))
    is_read = models.BooleanField('是否已读', default=False)
