from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def categories(request):
    template = loader.get_template('categories/categories.html')
    context = {

    }
    return HttpResponse(template.render(context,request))


def content(request,month):
    template = loader.get_template('categories/content.html')
    context = {
        "month": month,
    }
    return HttpResponse(template.render(context,request))
