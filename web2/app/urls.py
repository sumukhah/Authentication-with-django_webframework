from django.conf.urls import url
from . import views
urlpatterns = [

url(r'^$',views.home),
url(r'^regesteration/',views.regester),
url(r'^login/',views.login),
url(r'^logout/',views.logoff)
]
