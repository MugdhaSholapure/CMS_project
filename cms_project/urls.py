
from django.contrib import admin
from django.urls import path
from cmsapp.views import home,showdept,adddept,showstudent,addstudent,deletedept,deletestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("showdept/",showdept,name="showdept"),
    path("adddept/",adddept,name="adddept"),
    path("showstudent/",showstudent,name="showstudent"),
    path("addstudent/",addstudent,name="addstudent"),
    path("deletedept/<int:id>",deletedept,name="deletedept"),
    path("deletestudent/<int:id>",deletestudent,name="deletestudent"),
]
