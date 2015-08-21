from django.shortcuts import render
from schema.models import Template


def graph(request):
    templates = Template.objects.all()
    return render(request, 'graph.html', {'templates': templates})
