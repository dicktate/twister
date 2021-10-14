from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Create your views here.
def index(request):
    return HttpResponse("It works")

def timeline(request):
    response = "Todos los Posts" 
    #tl = Post.objects.order_by('-time')[:5]
    tl = Post.objects.all().order_by('-time')
    #template = loader.get_template('timeline/tl.html')
    context = { 'tl': tl }
    # return HttpResponse(template.render(context, request))
    return render(request, 'timeline/tl.html', context)

def detail(request, post_id):
    contenido = Post.objects.get(id=post_id)
    context = { 'contenido' : contenido }
    # print (Post.objects.get   post_id)
    # return HttpResponse('Post id = %i.' % post_id)
    return render(request, 'post/detail.html', context)