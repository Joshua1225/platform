from django.db import models
import os
from django.utils import timezone
# Create your models here.


def upload_paper_to(pid):
    return os.path.join('papers', pid)


def upload_avator_to(instance, filename):
    return os.path.join('avators', instance.user_id, filename)


def upload_documentation_to(instance, filename):
    return os.path.join('documentations', instance.user_id, filename)


class UnidentifiedAcademia(models.Model):
    """未认证的专家"""
    id = models.CharField(max_length=255, primary_key=True, verbose_name="专家ID", db_index=True)
    name = models.CharField(verbose_name="真实姓名", max_length=255)
    n_pubs = models.IntegerField(verbose_name="出版数", null=True)
    h_index = models.IntegerField(verbose_name="h指数", null=True)
    n_citation = models.IntegerField(verbose_name="总被引量", null=True)
    orgs = models.TextField(verbose_name="所在组织", null=True)
    tags = models.TextField(verbose_name="兴趣", null=True)
    pubs = models.TextField(verbose_name="出版物", null=True)
    """
    以上字段是网上下的数据里的字段，很多都会是空。
    n_pubs: 发布文献数量              int型
    h_index: 一个标记作者论文综合水平的指标    int型
    n_citation: 论文总被引量          int型
    orgs: 所在组织，格式为str: ['Department of Cardiothoracic Surgery,Xinhua Hospital,School of Medicine,Shanghai Jiao Tong University,Shanghai ,China']
    tags: 兴趣，格式为str w表示权重， t表示兴趣: [{'w': 1, 't': 'Gliding Arc Gas Discharge Æ Hexane Æ Decomposition Products Æ Plasma'}, {'w': 1, 't': 'Gliding Arc Gas Dischargeoxygenplasmavolatile Organic Compounds � Water Vapor'}]
    pubs: 论文，格式为str, i对应Papers的id，r表示作者在论文中的顺序  [{'i': '53e9a848b7602d970318eeb3', 'r': 3}, {'i': '53e9b53bb7602d970406ed59', 'r': 4}, {'i': '53e9a472b7602d9702d92f2f', 'r': 0}, {'i': '53e9b999b7602d970458a969', 'r': 0}]
    """
    position = models.CharField(max_length=255, null=True, verbose_name="任职")
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
        for i in range(5):
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
    username = models.CharField(primary_key=True, max_length=21, verbose_name="登录用户名")
    password = models.CharField(max_length=21, verbose_name="用户密码")
    name = models.CharField(max_length=21, verbose_name="用户名")
    credit = models.IntegerField(default=0, verbose_name="积分")
    interest = models.CharField(max_length=255, null=True, verbose_name="兴趣领域")
    email = models.EmailField(verbose_name="邮箱", unique=True, null=True)
    avator = models.ImageField(verbose_name="头像", null=True, upload_to=upload_avator_to)     # 这里有两个可选参数规定图片显示大长和宽，根据前端页面需要定，还需要一个default
    signature = models.TextField(null=True, verbose_name="个性签名")
    type = models.IntegerField(default=0, choices=((0, u"普通用户"), (1, u"专家")), verbose_name="用户类型")
    academia_id = models.ForeignKey(UnidentifiedAcademia, null=True, on_delete=models.PROTECT)
    follow = models.ManyToManyField(UnidentifiedAcademia, related_name='follow')
    collect = models.ManyToManyField(UnidentifiedAcademia, related_name='collect')

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
    authors = models.TextField(verbose_name="作者、机构及ID", null=True)
    year = models.IntegerField(null=True, verbose_name="发布年份")
    keywords = models.CharField(max_length=255, verbose_name="关键词", null=True)
    n_citation = models.IntegerField(default=0, verbose_name="被引量", null=True)
    references = models.TextField(verbose_name="参考文献", null=True)
    doc_type = models.CharField(max_length=255, verbose_name="文献类型", null=True)
    lang = models.CharField(max_length=255, null=True, verbose_name="论文语言")
    publisher = models.CharField(max_length=255, null=True, verbose_name="出版商")
    issn = models.CharField(max_length=255, null=True, verbose_name="ISSN号")
    isbn = models.CharField(max_length=255, null=True, verbose_name="ISBN号")
    doi = models.CharField(max_length=255, null=True, verbose_name="DOI码")
    pdf = models.FileField(verbose_name="pdf链接", null=True, blank=True, upload_to=upload_paper_to)
    url = models.TextField(verbose_name="外部链接", null=True)
    abstract = models.TextField(verbose_name="摘要", null=True)
    """
    doi是电子信息唯一索引码
    pdf:  //static.aminer.org/pdf/PDF/001/297/802/genetic_algorithms.pdf
    url(str型， 形式如右)：  ['http://dx.doi.org/10.1038/4371066a', 'http://www.ncbi.nlm.nih.gov/pubmed/16237400?report=xml&format=text', 'http://dx.doi.org/doi:10.1038/4371066a', 'http://www.nature.com/nature/journal/v437/n7062/full/4371066a.html']
    authors: 作者ID、机构、姓名，可能有很多个，并且每个作者这三个属性不一定全：[{'name': 'LIU Yu-qiong', 'org': 'School of Resource and Environmental Science,Wuhan University,Wuhan,Hubei ', 'id': '542a981ddabfae61d49943da'}]
    referecnes:
    """

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
                if dic.get('abstract') is not None and str(dic.get('title')).isdigit() is False:
                    Papers(id=dic.get('id'), title=str(dic.get('title')), authors=str(dic.get('authors')), year=dic.get('year'),
                           keywords=dic.get('keywords'), n_citation=dic.get('n_citation'), doc_type=dic.get('doc_type'),
                           lang=dic.get('lang'), issn=dic.get('issn'), isbn=dic.get('isbn'),
                           doi=dic.get('doi') , url=str(dic.get('url')), abstract=dic.get('abstract'),
                           references=dic.get('references')).save()


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

    type = models.IntegerField(choices=((1, "上传论文认证"), (2, "身份认证"), (3, "论文申诉"),(4, "专家推送"),(5, "论文推送")), verbose_name="站内信类型")

    content = models.TextField(verbose_name="用户内容", null=True)
    reply = models.TextField(verbose_name="管理员回复", null=True)
    time = models.TimeField(auto_now_add=True, verbose_name="生成时间")
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="用户ID")
    file = models.FileField(verbose_name="上传材料", null=True, upload_to=upload_documentation_to)
    object_id = models.CharField(max_length=255, verbose_name="目标资源")
    state = models.IntegerField(choices=((0, "未处理"), (1, "肯定"), (2, "否定")), default=0, verbose_name="受审状态")
    is_read = models.BooleanField(verbose_name="用户是否已阅", default=False)

    class Meta:
        db_table = 'Message'
        verbose_name = '站内信'
        verbose_name_plural = verbose_name
