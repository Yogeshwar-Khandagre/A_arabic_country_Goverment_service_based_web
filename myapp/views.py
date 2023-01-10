from fnmatch import fnmatchcase
from msilib.schema import File, tables
from turtle import update
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.http import HttpResponse
# from .models import MyModel
# from .testing import MyForm
# from django.contrib.auth.models import User

from .forms import *
from .models import *


# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def admindashbord(request):
    return render(request,"app/admindashbord.html")

def loginpage(request): 
    return render(request,"app/login.html")

def loginpage1(request): 
    return render(request,"app/my_admindash_backup.html")

def loginpage2(request): 
    return render(request,"app/login2.html")

def loginpage3(request): 
    return render(request,"app/login3.html")

def loginpage4(request): 
    return render(request,"app/login4.html")

def loginpage5(request): 
    return render(request,"app/login5.html")

def loginpage6(request): 
    return render(request,"app/login6.html")

def loginpage7(request): 
    return render(request,"app/login7.html")

def loginpage8(request): 
    return render(request,"app/login8.html")

def tableview(request): 
    return render(request,"app/basic-table.html")


def loginUser(request):
    if request.method == "POST":
        email= request.POST['Email']
        password= request.POST['Password']
        
        
        # print(Email)
        
        #cheaking Email id with DB

        user=User.objects.get(Email = email )
        if user:
            if user.Password == password:
                
                request.session['Email']= user.Email
                
                return render(request,"app/admindashbord.html",{'data':personalinfo.objects.all()})
                
            
            else:
                message="password does  not match" 
                # return render(request/"login.html",{'msg':message})
                return render(request,"app/login.html",{'msg':message})
                

        else:
            message='user does not exist'
            return render(request/"login.html",{'msg':message})


#show page view
def add(request):
    
    Fulladress1= request.POST['fulladress']
    District1=request.POST['district']
    Administration1=request.POST['administration']
    Office1=request.POST['office']
    Ministry1=request.POST['ministry']
    Area1=request.POST['area']
    Atonomous1=request.POST['atonomous']
    Disability1=request.POST['disability']
    Family1=request.POST['family']
    Mothername1=request.POST['mothername']
    Telephone1=request.POST['telephone']
    Partner1=request.POST['partner']
    City1=request.POST['city']
    Directorate1=request.POST['directorate']
    Ministryy1=request.POST['ministryy']
    Frname1=request.POST['frname']
    Teleph1=request.POST['teleph']
    Checkbox11=request.POST['checkbox1']
    Checkbox22=request.POST['checkbox2']
    Radio1=request.POST['yes_no1'] 
    Radio2=request.POST['yes_no2']
    Radio3=request.POST['yes_no4']
    Date1=request.POST['date1']
    Date2=request.POST['date2']
    File1 = request.FILES['file1']
    File2 = request.FILES['file2']
    File3 = request.FILES['file3']
    File4 = request.FILES['file4']

    Apartment1=request.POST.get('apartment')
    # file2 = request.POST['customInput2']

    # Frname1='Abhi'
    # print(Frname1)
    # print(Fulladress1,District1,Administration1,Office1,Ministry1,Area1,Atonomous1)
    
    print(Apartment1)

    
    newuser=personalinfo.objects.create(Fulladress=Fulladress1,District=District1,Administration=Administration1,
                                        Office=Office1,Ministry=Ministry1,Area=Area1,Atonomous=Atonomous1,
                                        Disability=Disability1,Family=Family1,
                                        Mothername=Mothername1,Telephone=Telephone1,Partner=Partner1,City=City1
                                        ,Directorate=Directorate1,Ministryy=Ministryy1,Frname=Frname1,Teleph=Teleph1,
                                        Checkbox1=Checkbox11,Checkbox2=Checkbox22,Radio1=Radio1,Radio2=Radio2,Radio3=Radio3,
                                        Date1=Date1,Date2=Date2,file1=File1,file2=File2,file3=File3,file4=File4,Apartment=Apartment1
                                        )
    
    # print(type(Frname1))
    
    messages.success(request,"Thank you for filling out your information.")
    return render(request,"form.html")
    


def showpage(request):
    #select * from table name
    #for fathing all the data from table
    all_data=Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})


#edit page view
def EditPage(request,pk):
    #fetching the data of particular ID
    get_data=Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def form(request):
    
    return render(request,"form.html")


def alldata(request):
    data=personalinfo.objects.all()
    return render(request,"app/admindashbord.html",{'data':data})


def alldata1(request): 
    data=personalinfo.objects.all().filter(Administration='هەولێر')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata2(request):
    data=personalinfo.objects.all().filter(Administration='زاخۆ')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata3(request):
    data=personalinfo.objects.all().filter(Administration='سلێمانی')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata4(request):
    data=personalinfo.objects.all().filter(Administration='دهۆك')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata5(request):
    data=personalinfo.objects.all().filter(Administration='هەڵەبجە')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata6(request):
    data=personalinfo.objects.all().filter(Administration='راپەڕین')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata7(request):
    data=personalinfo.objects.all().filter(Administration='گەرمیان')
    return render(request,"app/admindashbord.html",{'data':data})

def alldata8(request):
    data=personalinfo.objects.all().filter(Administration='سۆران')
    return render(request,"app/admindashbord.html",{'data':data})

def preview_record(request):
    id=request.GET['id']
    data=personalinfo.objects.all().filter(id=id)
    # print("----------------------------------------------------------------")
    # for i in data:
    #     print("----------->>>>>>>>",i.Frname)
    return render(request,"preview.html",{'data':data})


def demo(request):
    return render(request,"app/copy_form.html")




def delete_record(request):
    id=request.GET['id']
    personalinfo.objects.filter(id=id).delete()
    messages.success(request,"Data Deleted Successfully......")
    return redirect('/alldata')


def update_record(request):
    # id=request.GET['id']
    # data=personalinfo.objects.filter(id=id)
    # return render(request,"admindashbord.html",{'data':data})

    id=request.POST['id']
    Fulladress1= request.POST['fulladress']
    District1=request.POST['district']
    Administration1=request.POST['administration']
    Office1=request.POST['office']
    Ministry1=request.POST['ministry']
    Area1=request.POST['area']
    Atonomous1=request.POST['atonomous']
    Disability1=request.POST['disability']
    Family1=request.POST['family']
    Mothername1=request.POST['mothername']
    Partner1=request.POST['partner']
    City1=request.POST['city']
    Directorate1=request.POST['directorate']
    Ministryy1=request.POST['ministryy']
    Frname1=request.POST['frname']
    Teleph1=request.POST['teleph']
    Checkbox11=request.POST['checkbox1']
    Checkbox22=request.POST['checkbox2']
    Radio1=request.POST['yes_no1']
    Radio2=request.POST['yes_no2']
    Radio3=request.POST['yes_no4']
    Date1=request.POST['date1']
    Date2=request.POST['date2']
    Telephone1=request.POST['telephone']
    # File1 = request.FILES['file1']
    # File2 = request.FILES['file2']
    # File3 = request.FILES['file3']
    # File4 = request.FILES['file4']

    Apartment1=request.POST.get('apartment')
  
    personalinfo.objects.filter(id=id).update(Fulladress=Fulladress1,District=District1,Administration=Administration1,
                                        Office=Office1,Ministry=Ministry1,Area=Area1,Atonomous=Atonomous1,
                                        Disability=Disability1,Family=Family1,
                                        Mothername=Mothername1,Partner=Partner1,City=City1
                                        ,Directorate=Directorate1,Ministryy=Ministryy1,Frname=Frname1,Teleph=Teleph1,
                                        Checkbox1=Checkbox11,Checkbox2=Checkbox22,Radio1=Radio1,Radio2=Radio2,Radio3=Radio3,
                                        Date1=Date1,Date2=Date2,Telephone=Telephone1,
                                        Apartment=Apartment1)
    # ,File1=File1,File2=File2,File3=File3
    # return HttpResponse("OOOOOOOOOOKKKKKKKKKKKKK")

    data=personalinfo.objects.all()
    messages.success(request,"Successfully Updated Data...")
    return render(request,"app/admindashbord.html",{'data':data})
    # return render(request,"app/admindashbord.html")
  


from django.shortcuts import render, HttpResponse

# from .forms import MyfileUploadForm
# from .models import file_upload
        
     
        
def signin(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        
        app=User.objects.all().filter(Email=Email,Password=Password,is_active='Y')
        # app=User.objects.all()
        print('Abhiiiiiiiiiiiiiii')
        print(app)
        
        for item in app: 
            print(item.id,item.user_type)
            if item.user_type == "Admin":
                request.session['Email'] = Email
                return redirect ("/alldata")
            
            elif item.user_type == "هەولێر":
        
                request.session['Email'] = Email
                return redirect ("/alldata1")
            
            elif item.user_type == "سلێمانی":
                
                request.session['Email'] = Email
                return redirect ("/alldata3")
            
            elif item.user_type == "دهۆك":
                
                request.session['Email'] = Email
                return redirect ("/alldata4")

            elif item.user_type == "هەڵەبجە":
                
                request.session['Email'] = Email
                return redirect ("/alldata5")
            
            elif item.user_type == "راپەڕین":
                
                request.session['Email'] = Email
                return redirect ("/alldata6")
            
            
            elif item.user_type == "گەرمیان":
                
                request.session['Email'] = Email
                return redirect ("/alldata7")
            
            elif item.user_type == "سۆران":
                
                request.session['Email'] = Email
                return redirect ("/alldata8")
            
            elif item.user_type == "زاخۆ":
                
                request.session['Email'] = Email
                return redirect ("/alldata2")
            
        else:
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")
    
    

def logout(request):
    del request.session['Email']
    messages.success(request,("Successfully Logout..."))
    return redirect("/loginpage")



def signin1(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User5.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata1")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")


def signin2(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User6.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata2")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")


def signin3(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User7.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata3")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")


def signin4(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User8.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata4")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")


def signin5(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User9.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata5")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")

def signin6(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User10.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata6")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")


def signin7(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User11.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata7")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")

def signin8(request):
    if request.method == 'POST':
        Email = request.POST['Email']
        Password=request.POST['Password']
        
        app=User12.objects.all().filter(Email=Email,Password=Password)
        
        if app:
            request.session['Email'] = Email
            return redirect ("/alldata8")
        
        else:
            # request.session['Email'] = Email
            # return redirect ("/form")
            messages.success(request,"Wrong Email Id or Password")
            return render(request,"app/login.html")
        
    else:
        return HttpResponse("wrong")




def index(request):

    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        print(form.as_p)
        
        if form.is_valid():
            # name = form.cleaned_data['file_name']
            the_files1 = form.cleaned_data['files_data1']
            print(the_files1)
            the_files2 = form.cleaned_data['files_data2']
            print(the_files2)

            the_files3 = form.cleaned_data['files_data3']
            the_files4 = form.cleaned_data['files_data4']


            file_only(my_file1=the_files1, my_file2=the_files2, my_file3=the_files3, my_file4=the_files4).save()
            print(file_only)
            return HttpResponse("file upload")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':MyfileUploadForm()
        }      
        
        return render(request,'index.html', context)
        

def show_file(request):
    # this for testing 
    # id=request.GET['id']//
    id=request.GET['id']
    all_data=personalinfo.objects.all().filter(id=id)
    # all_data =personalinfo.objects.all().filter(id=id)

    context = {
        'data':all_data 
        }
    return render(request, 'view.html', context)


def change_password(request):
    change_data=User.objects.all()
    # return render(request,"app/admindashbord.html",{'change_data':change_data})
    return render(request,"app/change_password.html",{'change_data':change_data})