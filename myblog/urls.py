"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from myarticle import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
#   url(r'^(?P<my_args>\d+)/$', views.detail,name='detail'),
    url(r'^templateTest/$',views.templateTest,name = 'nowTime'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<id>\d+)/$',views.detail,name='details'),
    url(r'^login/', views.login,name='login'),
    url(r'^testAjax', views.testAjax),
   # url(r'^comments/',include('django_comments.urls'),name='comments'),
]
