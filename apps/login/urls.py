from django.conf.urls import url
from . import views
  # def method_to_run(request):
  #     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
  #     print "By the way, here's the request object that Django automatically passes us:", request
  #     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^register$', views.register, name = 'my_reg'),
    url(r'^logins$', views.logins, name = 'my_log'),
    url(r'^login/goback$', views.goback, name = 'my_back'),
    url(r'^success$', views.success, name = 'my_success'),
    url(r'^loginsuccess$', views.loginsuccess, name = 'my_login'),
    url(r'^clear$', views.clear, name = 'my_clear'),

 ]
