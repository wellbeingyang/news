from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import news
import random
# Create your views here.


def index(request):
    template = loader.get_template('news/index.html')
    a=random.sample(range(6974),20)
    context = {
        'news': [news.objects.all()[x] for x in a]
    }
    return HttpResponse(template.render(context, request))


def news_list(request):
    template = loader.get_template('news/list.html')
    context = {
		"news":news.objects.all()[:50]
    }
    return HttpResponse(template.render(context, request))


def news_content(request, id):
    template = loader.get_template('news/news.html')
    n = news.objects.get(id=id)
    context = {
        "id": n.id,
        "url": n.url,
        "title": n.title,
        "date": n.date,
		"image_url": n.image_url,
		"editor": n.editor,
		"text": eval(n.content.text)
    }
    return HttpResponse(template.render(context, request))
