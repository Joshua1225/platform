from haystack import indexes
from .models import Papers
# 原作者在代码中没有给出模型代码,这个模型里拥有的字段就是需要提供搜索的字段,建议保留模型字段中自增的主键字段id, 在我实际项目开发中发现如果不保留就无法实现搜索


# 索引模型类的名称必须是 模型类名称 + Index
class PapersIndex(indexes.SearchIndex, indexes.Indexable):
    """
    索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)  # 一般此字段约定为text　　 default_image_url = indexes.CharField(model_attr='default_image_url')
    def get_model(self):
        """返回建立索引的模型类"""
        return Papers

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_launched=True)
"""
说明: 
1.在DemoIndex建立的字段，都可以借助haystack由elasticsearch搜索引擎查询。
2.其中text字段声明为document=True，表名该字段是主要进行关键字查询的字段， 该字段的索引值可以由多个数据库模型类字段组成(是多个字段,不是多个数据库模型类,转者注)，具体由哪些模型类字段组成，我们用use_template=True表示后续通过模板来指明,其他字段都是通过model_attr选项指明引用数据库模型类的特定字段。
3.在 REST framework中，索引类的字段会作为查询结果返回数据的来源, 
"""