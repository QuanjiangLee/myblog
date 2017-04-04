from django.shortcuts import render
from django.http import HttpResponse
from myarticle.models import myArticle
from datetime import datetime

# Create your views here.
def home(request):
	postList = myArticle.objects.all()
	return render(request, 'home.html',{'postList':postList})
#    return HttpResponse("hello world,Django!")

def detail(request, my_args):
    post = myArticle.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, datetime = %s, content = %s" 
        % (post.title, post.category, post.datetime, post.content))
    return HttpResponse(str)

def templateTest(request):
	return render(request,'templateTest.html',{'nowTime':datetime.now()})
