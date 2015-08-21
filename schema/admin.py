from django.contrib import admin
from schema.models import Member
from schema.models import Field, Template

admin.site.register(Member)
admin.site.register(Field)
admin.site.register(Template)
