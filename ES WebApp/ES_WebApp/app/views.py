from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
DIRNAME = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'site-templates/'),
)


def index(request):


    file = open('/var/tmp/coleman/API.txt', 'r')
    line = file.readline()
    WLP = int(line.split()[1])

    template = loader.get_template("app/index.html")
    context = {
        "WLP": WLP,
    }
    return render(request, 'app/index.html', context=context)
    return HttpResponse(template.render(context, request))