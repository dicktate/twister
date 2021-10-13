from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.
def index(request):
    return HttpResponse("It works")

def timeline(request):
    response = "Todos los Posts" 
    tl = Post.objects.order_by('-time')[:5]
    #print(tl)
    #op = '<li>'.join([p.text for p in tl])
    template = loader.get_template('timeline/tl.html')
    context = { 'tl': tl }
    print(HttpResponse(template.render(context, request)))
    return HttpResponse(template.render(context, request))
    # return render(request, 'timeline/tl.html', context)
    # return HttpResponse(response),

