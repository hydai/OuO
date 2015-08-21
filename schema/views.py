from schema.models import Member
from django.shortcuts import render


def save_userdata(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        try:
            profile = Member.objects.get(user_id=user.id)
        except Member.DoesNotExist:
            profile = Member(user_id=user.id)
        profile.uuid = response.get('id')
        profile.save()


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'index.html')
