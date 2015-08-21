from django.contrib import admin
from schema.models import Field, Mapping, Template, Graph, Member


admin.site.register(Member)
admin.site.register(Field)
admin.site.register(Mapping)
admin.site.register(Template)
admin.site.register(Graph)
