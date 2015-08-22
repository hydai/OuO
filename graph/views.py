from django.shortcuts import render, get_object_or_404
from schema.models import Template, Mapping, Member, Graph
from forms import CreateForm
import json
from django.http import HttpResponseRedirect


def gallery(request):
    templates = Template.objects.all()
    return render(request, 'graph.html', {'templates': templates})


def explore(request, tid=None):
    if tid:
        template = get_object_or_404(Template, id=tid)
        graphs = Graph.objects.filter(template=template)
    else:
        graphs = Graph.objects.all()
    return render(request, 'explore.html', {'graphs': graphs})


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
                return HttpResponseRedirect('/graph/result/%d' % graph.id)

    return render(request, 'create_graph.html', {'form': form, 'fields': fields})


def mapping_json(request, gid):
    graph = get_object_or_404(Graph, id=gid)

    json_arr = json.loads(graph.data_src)
    for i in range(len(json_arr)):
        for mapping in graph.mappings.all():
            if mapping.field.fname != mapping.onto:
                json_arr[i][mapping.field.fname] = json_arr[i][mapping.onto]
                del json_arr[i][mapping.onto]
    return json.dumps(json_arr)


def result(request, gid):
    graph = get_object_or_404(Graph, id=gid)
    json_arr = mapping_json(request, gid)
    return render(request, 'result.html', {'graph': graph, 'json_arr': json_arr})
