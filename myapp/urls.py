# from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    # path("",views.InsertPageView,name='insertpage'),
    # path("insert/",views.InsertData,name="insert"),
    path("",views.form,name="form"),
    path("add/",views.add,name="add"),
    path("admindashbord/",views.admindashbord,name="admindashbord"),
    path("alldata/",views.alldata,name="alldata"),
    path("loginpage/",views.loginpage,name='loginpage'),
    path("loginUser/",views.loginUser,name='loginUser'),
    path("basic-table/",views.tableview,name='table'),
    path("demo/",views.demo,name="demo"),
    path("delete_record/",views.delete_record,name='delete_record'),
    path("preview_record/",views.preview_record,name="preview_record"),
    path("update_record/",views.update_record,name='update_record'),
    path("signin/",views.signin,name='signin'),
    path("signin1/",views.signin1,name='signin1'),
    path("alldata1/",views.alldata1,name='alldata1'),
    path("loginpage1/",views.loginpage1,name='loginpage1'),
    path("signin2/",views.signin2,name='signin2'),
    path("alldata2/",views.alldata2,name='alldata2'),
    path("loginpage2/",views.loginpage2,name='loginpage2'),
    path("signin3/",views.signin3,name='signin3'),
    path("alldata3/",views.alldata3,name='alldata3'),
    path("loginpage3/",views.loginpage3,name='loginpage3'),
    path("signin4/",views.signin4,name='signin4'),
    path("alldata4/",views.alldata4,name='alldata4'),
    path("loginpage4/",views.loginpage4,name='loginpage4'),
    path("signin5/",views.signin5,name='signin5'),
    path("alldata5/",views.alldata5,name='alldata5'),
    path("loginpage5/",views.loginpage5,name='loginpage5'),
    path("signin6/",views.signin6,name='signin6'),
    path("alldata6/",views.alldata6,name='alldata6'),
    path("loginpage6/",views.loginpage6,name='loginpage6'),
    path("signin7/",views.signin7,name='signin7'),
    path("alldata7/",views.alldata7,name='alldata7'),
    path("loginpage7/",views.loginpage7,name='loginpage7'),
    path("signin8/",views.signin8,name='signin8'),
    path("alldata8/",views.alldata8,name='alldata8'),
    path("loginpage8/",views.loginpage8,name='loginpage8'),
    path("logout/",views.logout,name='logout'),
        #for demo
    path('ind', views.index, name="home"),
    path('show_file', views.show_file, name="show_file"),
    path('change_password',views.change_password,name="change_password")
    
    
    
    
    # path('', views.index, name="home"),
    # path('view', views.downlodfile, name="view")
    


    # path("showpage/",views.showpage,name="showpage"),
    # path("editpage/<int:pk>",views.EditPage,name="editpage"),
    # path("update/<int:pk>",views.UpdateData,name="update"),
    # path("delete/<int:pk>",views.DeleteData,name="delete"),
    

    ]
