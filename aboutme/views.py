from django.http import HttpResponse
from django.template import loader
from .models import PersonalInfo, Project, ProjectPicture


def index(request):
    template = loader.get_template('aboutme/index.html')
    personal_info = PersonalInfo.objects.all()
    context = {
        'personal_info': personal_info,
    }
    return HttpResponse(template.render(context, request))
