from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):


    file = open('./var/tmp/coleman/API.txt', 'r')
    line = file.getline()
    WLP = int(line.split()[1])

    template = loader.get_template("app/index.html")
    context = {
        "WLP": WLP,
    }
    return HttpResponse(template.render(context, request))