"""salmanBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from posts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin_which_belongs_to_salman_barani/', admin.site.urls),
    url(r'^$', views.home),
    #regx => ?p(announce the next part is variable,inside is <variable_name>)
    #as long is it's a number and is between [0-9], no matter what
    # long it has; it's going to assign to <variable_name>
    
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name='post_detail'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)