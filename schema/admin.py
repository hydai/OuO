from django.contrib import admin
<<<<<<< HEAD
from schema.models import Field, Mapping, Template, Graph
=======
from schema.models import Member
from schema.models import Field, Template
>>>>>>> 533adbabdec2f98b3eb37d7ad6855cf162bfbd6f

admin.site.register(Member)
admin.site.register(Field)
admin.site.register(Mapping)
admin.site.register(Template)
admin.site.register(Graph)
