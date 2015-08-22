from django.shortcuts import render, get_object_or_404
from schema.models import Template, Mapping, Member
from forms import CreateForm


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


    return render(request, 'create_graph.html', {'form': form, 'fields': fields})
