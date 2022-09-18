from re import template
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def about(request):
    template = loader.get_template('infos/main.html')
    return HttpResponse(template.render(request=request))
    


def me(request):
    template = loader.get_template('infos/me.html')
    return HttpResponse(template.render(request=request))

    

def contact(request):
    if request.method =='POST':
        return about(request)
    elif request.method == 'GET':
        template = loader.get_template('infos/contact.html')
        return HttpResponse(template.render(request=request))

