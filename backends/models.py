from django.db import models
import uuid
from django.utils import timezone
# Create your models here.

# ImageField 和 FileField 都有up_load参数控制上传文件的位置， 目前没填


class UnidentifiedAcademia(models.Model):
    """未认证的专家"""
    id = models.CharField(max_length=255, primary_key=True, verbose_name="专家ID", db_index=True)
    name = models.CharField(verbose_name="真实姓名", max_length=255)
    n_pubs = models.IntegerField(verbose_name="出版数", null=True)
    h_index = models.IntegerField(verbose_name="h指数", null=True)
    n_citation = models.IntegerField(verbose_name="总被引量", null=True)
    orgs = models.TextField(verbose_name="曾经组织", null=True)
    # org = models.IntegerField(verbose_name="现任组织", null=True)
    tags = models.TextField(verbose_name="兴趣", null=True)
    # tags_t = models.CharField(max_length=65535, verbose_name="兴趣领域", null=True)
    # tags_w = models.IntegerField(verbose_name="兴趣权重", null=True)
    pubs = models.TextField(verbose_name="出版物", null=True)
    # institute = models.CharField(max_length=255, null=True, verbose_name="机构")
    position = models.CharField(max_length=255, null=True, verbose_name="任职")
    # field = models.TextField(null=True, verbose_name="专攻领域")
    experience = models.TextField(null=True, verbose_name="项目经验")
    education = models.TextField(null=True, verbose_name="教育经历")
    tendency = models.TextField(null=True, verbose_name="合作意向")

    class Meta:
        db_table = 'UnidentifiedAcademia'
        verbose_name = "未认证专家"
        verbose_name_plural = verbose_name

    @staticmethod
    def data_import():
        import json
        strs = 'aminer_authors_'
        for i in range(1, 6):
            strs += str(i)
            strs += ".txt"
            with open(strs) as f:
                for line in f:
                    dic = json.loads(line)
                    UnidentifiedAcademia(id=dic.get('id'), name=dic.get('name'), n_pubs=dic.get('n_pubs'),
                                          orgs=str(dic.get('orgs')), position=dic.get('position'),
                                          n_citation=dic.get('n_citation'), h_index=dic.get('h_index'),
                                          tags=str(dic.get('tags')), pubs=str(dic.get('pubs'))).save()


class Users(models.Model):
    """用户"""
    user_id = models.UUIDField(default=uuid.uuid4, max_length=21, primary_key=True, db_index=True, verbose_name="用户ID", editable=False)
    password = models.CharField(max_length=21, verbose_name="用户密码")
    name = models.CharField(max_length=21, verbose_name="用户名字")
    credit = models.IntegerField(default=0, verbose_name="积分")
    interest = models.CharField(max_length=255, null=True, verbose_name="兴趣领域")
    email = models.EmailField(null=True, verbose_name="邮箱")
    avator = models.ImageField(verbose_name="头像", null=True)     # 这里有两个可选参数规定图片显示大长和宽，根据前端页面需要定，还需要一个default
    signature = models.TextField(null=True, verbose_name="个性签名")
    type = models.IntegerField(default=0, choices=((0, u"普通用户"), (1, u"专家")), verbose_name="用户类型")
    academia_id = models.ForeignKey(UnidentifiedAcademia, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'User'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Administrators(models.Model):
    """管理员"""
    admin_id = models.CharField(max_length=21, primary_key=True, db_index=True, verbose_name="管理员ID")
    password = models.CharField(max_length=21, verbose_name="密码")

    class Meta:
        db_table = 'Administrator'
        verbose_name = '管理员'
        verbose_name_plural = verbose_name


class Papers(models.Model):
    """论文"""
    id = models.CharField(max_length=255, primary_key=True, db_index=True, verbose_name="论文ID")
    title = models.CharField(max_length=255, verbose_name="论文标题", null=True)
    # authors_name = models.CharField(max_length=255, verbose_name="论文作者")
    # authors_institute = models.CharField(max_length=255, null=True, verbose_name="作者机构")
    authors = models.TextField(verbose_name="作者、机构及ID",null=True)
    # venue = models.CharField(max_length=255, null=True, verbose_name="论文出处")         # 如会议名称
    year = models.IntegerField(null=True, verbose_name="年份")
    keywords = models.CharField(max_length=255, verbose_name="关键词", null=True)
    # field_of_study = models.CharField(max_length=255, null=True, verbose_ngitame="论文领域")
    n_citation = models.IntegerField(default=0, verbose_name="被引量", null=True)
    references = models.TextField(verbose_name="参考文献", null=True)
    # page_stat
    # page_end
    doc_type = models.CharField(max_length=255, verbose_name="文献类型", null=True)
    lang = models.CharField(max_length=255, null=True, verbose_name="论文语言")
    publisher = models.CharField(max_length=255, null=True, verbose_name="出版商")
    # volumn
    # issue
    issn = models.CharField(max_length=255, null=True, verbose_name="ISSN号")
    isbn = models.CharField(max_length=255, null=True, verbose_name="ISBN号")
    doi = models.CharField(max_length=255, null=True, verbose_name="DOI码")
    pdf = models.TextField(verbose_name="pdf链接", null=True)
    url = models.TextField(verbose_name="外部链接", null=True)
    abstract = models.TextField(verbose_name="摘要", null=True)
    # belonging = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, verbose_name="所属专家")

    class Meta:
        db_table = 'Paper'
        verbose_name = '论文'
        verbose_name_plural = verbose_name

    @staticmethod
    def data_import():
        import json
        with open('aminer_papers_0.txt') as f:
            for line in f:
                dic = json.loads(line)
                Papers(id=dic.get('id'), title=str(dic.get('title')), authors=str(dic.get('authors')), year=dic.get('year'),
                       keywords=dic.get('keyword'), n_citation=dic.get('n_citation'), doc_type=dic.get('doc_type'),
                       lang=dic.get('lang'), publisher=dic.get('publisher'), issn=dic.get('issn'), isbn=dic.get('isbn'),
                       doi=dic.get('doi'), pdf=dic.get('pdf'), url=str(dic.get('url')),
                       abstract=dic.get('abstract')).save()


class Trades(models.Model):
    """交易记录"""
    price = models.IntegerField(default=0, verbose_name="积分价格")
    buyer_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="买者ID")
    paper_id = models.ForeignKey(Papers, on_delete=models.CASCADE, verbose_name="论文ID")
    time = models.DateField(auto_now_add=True, verbose_name="交易时间")

    class Meta:
        db_table = 'Trade'
        verbose_name = '交易'
        verbose_name_plural = verbose_name


class Messages(models.Model):
    """站内信"""
    type = models.IntegerField(choices=((1, "上传论文认证"), (2, "身份认证"), (3, "论文归属权申诉")), verbose_name="站内信类型")
    content = models.TextField(verbose_name="用户内容", null=True)
    reply = models.TextField(verbose_name="管理员回复", null=True)
    time = models.TimeField(auto_now_add=True, verbose_name="生成时间")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="用户ID")
    file = models.FileField(verbose_name="上传材料", null=True)
    object_id = models.CharField(max_length=255, verbose_name="目标资源")
    state = models.IntegerField(choices=((0, "未处理"), (1, "肯定"), (2, "否定")), default=0, verbose_name="受审状态")
    is_read = models.BooleanField(verbose_name="用户是否已阅", default=False)

    class Meta:
        db_table = 'Message'
        verbose_name = '站内信'
        verbose_name_plural = verbose_name


