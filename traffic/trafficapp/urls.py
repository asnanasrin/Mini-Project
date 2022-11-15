from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    # path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
    path('home/',views.home,name="home"),
    path('case/',views.case,name="case"),
    path('view/',views.view,name="view"),
    path('userreg/',views.userreg,name="userreg"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userhome',views.userhome,name="userhome"),
    path('result/',views.result1,name="result"),
    path('userlog/',views.userlog,name="userlog"),
    path('viewcase/',views.viewcase,name="viewcase"),
    path('viewchallan/',views.viewchallan,name="viewchallan")
   
]