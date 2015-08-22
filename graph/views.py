from django.shortcuts import render, get_object_or_404
from schema.models import Template, Mapping, Member
from forms import CreateForm
import json
from django.http import JsonResponse

def gallery(request):
    templates = Template.objects.all()
    return render(request, 'graph.html', {'templates': templates})


def create(request, tid):
    template = get_object_or_404(Template, id=tid)
    fields = template.fields.all()
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            graph = form.save(commit=False)
            graph.template = template
            graph.owner = Member.objects.get(user=request.user)
            graph.save()
            for field in fields:
                onto = request.POST.get(field.fname, '')
                mapping = Mapping.objects.create(field=field, onto=onto)
                graph.mappings.add(mapping)
                graph.save()

            json_arr = json.loads(graph.data_src)
            print json_arr
            for i in range(len(json_arr)):
                for mapping in graph.mappings.all():
                    json_arr[i][mapping.field.fname] = json_arr[i][mapping.onto]
                    del json_arr[i][mapping.onto]
            print json_arr
            return JsonResponse(json_arr, safe=False)


    return render(request, 'create_graph.html', {'form': form, 'fields': fields})
