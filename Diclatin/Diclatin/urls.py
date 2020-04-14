from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', views.hello, name="hello"),
    url(r'^translate/', views.translate, name="translatepage"),
    url(r'^about/', views.about, name="about")
]
