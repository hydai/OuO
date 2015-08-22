from django import forms
from schema.models import Template, Graph


class CreateForm(forms.ModelForm):
    class Meta:
        model = Graph
        fields = ('gname', 'description', 'data_src')
