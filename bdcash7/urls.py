"""bdcash7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from bdcash7 import views
from django.conf.urls.static import static
from bdcash7.settings import MEDIA_ROOT
from games.views import game1,game2,game3, game4, game5, game6
from User.views import singup,handlelogin,handlelogout, password_change, user_statement
from all_payments.views import make_deposite,make_accept,make_widthdrawal,accept
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("game1/",game1),
    path("game2/",game2),
    path("game3/",game3),
    path("game4/",game4),
    path("game5/",game5),
    path("game6/",game6),
    path("singup/",singup, name ="singup"),
    path("singin/",handlelogin , name ="handelsingin"),
    path("logout/",handlelogout, name = "handlelogout"),
    path("deposite/",views.deposite_money , name ="deposite_money"),
    # path("admin/all_payments/deposite_request/<int:id/change/",depsite_to_user)
    path("wallet/",views.wallet),
    path("login_user_password_change/",password_change, name ="change_pass"),
    path("widthdrawl_request/",views.widthdrawl_request,name="widthdrawl_request"),
    path("user_statement",user_statement,name ="user_statement"),
    path("make_deposite/<int:id>/",make_deposite, name ="make_deposite"),
    path("make_accept/<int:id>/",make_accept),
    path('make_widthdrawal/<int:id>/',make_widthdrawal),
    path("accept/<int:id>/",accept),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)