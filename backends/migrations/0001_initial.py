# Generated by Django 2.2.1 on 2019-06-04 19:51

import backends.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('admin_id', models.CharField(db_index=True, max_length=21, primary_key=True, serialize=False, verbose_name='管理员ID')),
                ('password', models.CharField(max_length=21, verbose_name='密码')),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'Administrator',
            },
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, verbose_name='论文ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='论文标题')),
                ('authors', models.TextField(null=True, verbose_name='作者、机构及ID')),
                ('year', models.IntegerField(null=True, verbose_name='发布年份')),
                ('keywords', models.CharField(max_length=255, null=True, verbose_name='关键词')),
                ('n_citation', models.IntegerField(default=0, null=True, verbose_name='被引量')),
                ('references', models.TextField(null=True, verbose_name='参考文献')),
                ('doc_type', models.CharField(max_length=255, null=True, verbose_name='文献类型')),
                ('lang', models.CharField(max_length=255, null=True, verbose_name='论文语言')),
                ('publisher', models.CharField(max_length=255, null=True, verbose_name='出版商')),
                ('issn', models.CharField(max_length=255, null=True, verbose_name='ISSN号')),
                ('isbn', models.CharField(max_length=255, null=True, verbose_name='ISBN号')),
                ('doi', models.CharField(max_length=255, null=True, verbose_name='DOI码')),
                ('pdf', models.FileField(blank=True, null=True, upload_to=backends.models.upload_paper_to, verbose_name='pdf链接')),
                ('url', models.TextField(null=True, verbose_name='外部链接')),
                ('abstract', models.TextField(null=True, verbose_name='摘要')),
            ],
            options={
                'verbose_name': '论文',
                'verbose_name_plural': '论文',
                'db_table': 'Paper',
            },
        ),
        migrations.CreateModel(
            name='UnidentifiedAcademia',
            fields=[
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, verbose_name='专家ID')),
                ('name', models.CharField(max_length=255, verbose_name='真实姓名')),
                ('n_pubs', models.IntegerField(null=True, verbose_name='出版数')),
                ('h_index', models.IntegerField(null=True, verbose_name='h指数')),
                ('n_citation', models.IntegerField(null=True, verbose_name='总被引量')),
                ('orgs', models.TextField(null=True, verbose_name='所在组织')),
                ('tags', models.TextField(null=True, verbose_name='兴趣')),
                ('pubs', models.TextField(null=True, verbose_name='出版物')),
                ('position', models.CharField(max_length=255, null=True, verbose_name='任职')),
                ('experience', models.TextField(null=True, verbose_name='项目经验')),
                ('education', models.TextField(null=True, verbose_name='教育经历')),
                ('tendency', models.TextField(null=True, verbose_name='合作意向')),
            ],
            options={
                'verbose_name': '未认证专家',
                'verbose_name_plural': '未认证专家',
                'db_table': 'UnidentifiedAcademia',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=21, primary_key=True, serialize=False, verbose_name='登录用户名')),
                ('password', models.CharField(max_length=21, verbose_name='用户密码')),
                ('name', models.CharField(max_length=21, verbose_name='用户名')),
                ('credit', models.IntegerField(default=0, verbose_name='积分')),
                ('interest', models.CharField(max_length=255, null=True, verbose_name='兴趣领域')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='邮箱')),
                ('avator', models.ImageField(null=True, upload_to=backends.models.upload_avator_to, verbose_name='头像')),
                ('signature', models.TextField(null=True, verbose_name='个性签名')),
                ('type', models.IntegerField(choices=[(0, '普通用户'), (1, '专家')], default=0, verbose_name='用户类型')),
                ('academia_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backends.UnidentifiedAcademia')),
                ('collect', models.ManyToManyField(related_name='collect', to='backends.Papers')),
                ('follow', models.ManyToManyField(related_name='follow', to='backends.UnidentifiedAcademia')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='积分价格')),
                ('time', models.DateField(auto_now_add=True, verbose_name='交易时间')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Users', verbose_name='买者ID')),
                ('paper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Papers', verbose_name='论文ID')),
            ],
            options={
                'verbose_name': '交易',
                'verbose_name_plural': '交易',
                'db_table': 'Trade',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, '上传论文认证'), (2, '身份认证'), (3, '论文申诉'), (4, '专家推送'), (5, '论文推送')], verbose_name='站内信类型')),
                ('content', models.TextField(null=True, verbose_name='用户内容')),
                ('reply', models.TextField(null=True, verbose_name='管理员回复')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='生成时间')),
                ('file', models.FileField(null=True, upload_to=backends.models.upload_documentation_to, verbose_name='上传材料')),
                ('object_id', models.CharField(max_length=255, verbose_name='目标资源')),
                ('state', models.IntegerField(choices=[(0, '未处理'), (1, '肯定'), (2, '否定')], default=0, verbose_name='受审状态')),
                ('is_read', models.BooleanField(default=False, verbose_name='用户是否已阅')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backends.Users', verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '站内信',
                'verbose_name_plural': '站内信',
                'db_table': 'Message',
            },
        ),
    ]
