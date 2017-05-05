import json
from django.shortcuts import render
from django.http import HttpResponse
from myarticle.models import myArticle
from datetime import datetime
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	postList = myArticle.objects.all()
	for post in postList:
		if len(str(post.content)) > 200:
			post.content = str(post.content)[0:200]
		else:
			continue
	archiList = myArticle.objects.all()
	return render(request, 'home.html',{'postList':postList,'archiList':archiList})
#    return HttpResponse("hello world,Django!")

def  detail(request, id):
	try:
		post = myArticle.objects.get(id=str(id))
	except myArticle.DoesNotExist:
		raise Http404
	archiList = myArticle.objects.all()
	return render(request, 'post.html', {'post': post,'archiList': archiList})	
'''
def archives(request):
	try:
		archiList = myArticle.objects.all()
	except myArticle.DoesNotExist:
		raise Http404
	return render(request,'archives.html',{'archiList': archiList})

def detail(request, my_args):
    post = myArticle.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, datetime = %s, content = %s" 
        % (post.title, post.category, post.datetime, post.content))
    return HttpResponse(str)
'''
def templateTest(request):
	return render(request,'templateTest.html',{'nowTime':datetime.now()})

def login(request):
	return render(request,'login.html')
'''
def archives(request):
	try:
		postList = myArticle.objects.all()
	except myArticle.DoesNotExist:
		raise Http404
	return render(request,'archives.html',{'post_list' : postList,'error': False})
'''
@csrf_exempt
def testAjax(request):
	print (request.method)
	#a = request.POST.get('hello','')
	#a = request.body.decode("utf-8")
	a={"hello":"world"}
	print(a)
	return HttpResponse(json.dumps(a), content_type='application/json')
