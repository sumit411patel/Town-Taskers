from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth,messages
from workers.models import *
from myadmin.models import *
from user.models import *
import os


# Create your views here.

def home(request):
    result1 = Category.objects.all()
    result2 = Sub_category.objects.all()
    context = {'categories':result1,'subcategories':result2}
    return render(request, 'workers/home.html' ,context)

def worker_dashboard(request):
    result = Post_problem.objects.all()
    context = {'urequests':result}
    return render(request, 'workers/worker_dashboard.html' ,context)

def about(request):
    context = {}
    return render(request, 'workers/about.html' ,context)

def worker_register(request):
    result1 = Category.objects.all()
    result2 = Sub_category.objects.all()
    result3 = City.objects.all()
    result4 = Area.objects.all()
    context = {'categories':result1, 'sub_categories':result2,'cities':result3,'areas':result4}
    return render(request, 'workers/worker_register.html' ,context)

def worker_store(request):
    #user
    fname = request.POST['fname']
    lname = request.POST['lname']
    uname = request.POST['uname']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']


    #profile
    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    dob = request.POST['dob']
    city = request.POST['cityname']
    area = request.POST['areaname']
    category = request.POST['categoryname']
    subcategory = request.POST['subcategoryname']
    workdesc = request.POST['wdesc']
    myfile = request.FILES['wimg']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)

    if password == cpassword:
        result = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
        Worker_profile.objects.create(address=address,contact=contact,gender=gender,date_of_birth=dob,city_id=city,area_id=area,category_id = category,subcategory_id=subcategory,work_description = workdesc, worker_image=myfile,worker_id=result.id)
        return redirect('/workers/worker_register')
    else:
        messages.warning(request,'Missmatch Password')


def worker_edit_profile(request):
    result1 = City.objects.all()
    result2 = Area.objects.all()
    result3 = Category.objects.all()
    result4 = Sub_category.objects.all()
    id = request.user.id
    result = Worker_profile.objects.get(worker_id=id)
    context = {'result':result,'cities':result1,'areas':result2,'categories':result3,'sub_categories':result4}
    return render(request, 'workers/worker_edit_profile.html' ,context)


def worker_update(request,id):
    id1 = request.user.id
    myfile = request.FILES['wimg']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)

    data = {
            'contact' : request.POST['contact'],
            'address' : request.POST['address'],
            'gender' : request.POST['gender'],
            'date_of_birth' : request.POST['dob'],
            'city_id' : request.POST['cityname'],
            'area_id' : request.POST['areaname'],
            'worker_image' : myfile.name,
            'category_id' : request.POST['categoryname'],
            'subcategory_id' : request.POST['subcategoryname'],
            'work_description' : request.POST['wdesc']
           }
    Worker_profile.objects.update_or_create(pk=id,defaults=data)
    data1 = {
            'first_name' : request.POST['fname'],
            'last_name' : request.POST['lname'],
            'username' : request.POST['uname'],
            'email' : request.POST['email']
            }

    worker = User.objects.update_or_create(pk=id1,defaults=data1)
    return redirect('/workers/worker_edit_profile')

def login(request):
    context = {}
    return render(request, 'workers/login.html' ,context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username,password=password)

    if result is None:
        messages.warning(request,'Invalid Username and Password')
        return redirect('/workers/login')

    else:
        if Worker_profile.objects.filter(worker_id=result.id).exists():
            res = Worker_profile.objects.get(worker_id=result.id)
            if res.status == 'disable':
                messages.warning(request,'Worker is not Verified yet')
                return redirect('/workers/login')
            else:
                auth.login(request, result)
                return redirect('/workers/home')

        else:
            messages.warning(request,'Invalid User Try again to Logged in')
            return redirect('/workers/login')


def logout(request):
    auth.logout(request)
    return redirect('/workers/login')

def contact(request):
    context = {}
    return render(request, 'workers/contact.html', context)

def contact_store(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    contact_cat = request.POST['cat']
    message = request.POST['message']

    Contact_us.objects.create(name=name, email = email,contact=contact,contact_category=contact_cat,message=message)
    messages.success(request,'Thank You for sharing this with us,we will reply by email as soon as possible')

    return redirect('/workers/contact')    

def user_rate(request):
    context = {}
    return render(request, 'workers/user_rate.html' ,context)

def user_request(request):
    id = request.user.id
    result = Worker_profile.objects.get(worker_id=id)
    cate_id = result.category_id
    result1 = Post_problem.objects.filter(category_id=cate_id)
    context = {'result': result,'urequests':result1}
    return render(request, 'workers/user_request.html' ,context)

def view_user_request(request,id):
    worker_id = request.user.id
    result1 = Worker_profile.objects.get(worker_id=worker_id)
    result = Post_problem.objects.get(pk=id)

    if Apply_request.objects.filter(user_post_id=id, worker_id=worker_id).exists():
        status = 'yes'
    else:
        status = 'no'

    context = {'urequests':result,'result1':result1,'status':status}
    return render(request,'workers/view_user_request.html', context)

def apply_request(request,id):
    
    worker_id = request.user.id
    result1 = Worker_profile.objects.get(worker_id=worker_id)
    result = Post_problem.objects.get(pk=id)
    context = {'result':result,'result1':result1}
    return render(request, 'workers/apply_request.html' ,context)


def apply_request_store(request,id):
    application = request.POST['apply']
    reason = request.POST['reason'] 
    id1 = request.user.id

    Apply_request.objects.create(application=application, reason = reason, worker_id=id1, user_post_id = id)
    return redirect('/workers/user_request')