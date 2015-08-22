#--encoding:utf8--
from django import forms
from schema.models import Template, Graph


class CreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.fields['gname'].label = '圖表名稱'
        self.fields['description'].label = '敘述'
        self.fields['data_src'].label = '資料'

    class Meta:
        model = Graph
        fields = ('gname', 'description', 'data_src')
