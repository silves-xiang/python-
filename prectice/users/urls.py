from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
app_name = 'users'
urlpatterns = [
    #登陆界面
    #url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^regester/$',views.regester,name='regester'),
]