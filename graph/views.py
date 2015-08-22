from django.shortcuts import render, get_object_or_404
from schema.models import Template
from forms import CreateForm


def gallery(request):
    templates = Template.objects.all()
    return render(request, 'graph.html', {'templates': templates})


def create(request, tid):
    template = get_object_or_404(Template, id=tid)
    fields = template.fields.all()

    form = CreateForm(initial={'template': template})
    if request.method == 'POST':
        form = CreateForm(request.POST, initial={'template': template})
        if form.is_valid():
            print 'valid'
        else:
            print 'gg'
        print request.POST
    return render(request, 'create_graph.html', {'form': form, 'fields': fields})
