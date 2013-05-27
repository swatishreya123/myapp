# Create your views here.

from django.template import Context, loader

from polls.models import Poll

def index(request):
    latest_home_list = home.objects.order_by('message')[:5]
    template = loader.get_template('home/index.html')
    context = Context({
        'latest_home_list': latest_home_list,
    })
    return HttpResponse(template.render(context))
