from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth,messages
from user.models import *
from myadmin.models import *
from workers.models import *
import os

# Create your views here.

def get_subcategories_by_id(request):
    id = request.GET['cat_id']
    result = Sub_category.objects.filter(category_id=id)
    context = {'result':result}
    return render(request, 'user/get_subcategories.html' ,context)

def home(request):
    result1 = Category.objects.all()
    result2 = Sub_category.objects.all()
    context = {'categories':result1,'subcategories':result2}
    return render(request, 'user/home.html' ,context)

def about(request):
    context = {}
    return render(request, 'user/about.html' ,context)

def login(request):
    context = {}
    return render(request, 'user/login.html' ,context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(request, username=username,password=password)

    if result is None:
        messages.warning(request,'Invalid Username and Password')
        return redirect('/user/login')

    else:
        if User_profile.objects.filter(user_id=result.id).exists():
            auth.login(request, result)
            return redirect('/user/home')
        else:
            messages.warning(request,'Invalid User Try to Logged in')
            return redirect('/user/login')


def logout(request):
    auth.logout(request)
    return redirect('/user/login')



def user_register(request):
    result1 = City.objects.all()
    result2 = Area.objects.all()
    context = {'cities':result1,'areas':result2}
    return render(request, 'user/user_register.html' ,context)

def user_store(request):
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
    myfile = request.FILES['uimg']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)

    if password == cpassword:
        result = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
        User_profile.objects.create(address=address,contact=contact,gender=gender,date_of_birth=dob,city_id=city,area_id=area,user_image=myfile,user_id=result.id)
        return redirect('/user/user_register')
    else:
        messages.warning(request,'Missmatch Password')


def user_edit_profile(request):
    result1 = City.objects.all()
    result2 = Area.objects.all()
    id = request.user.id
    result = User_profile.objects.get(user_id=id)
    context = {'result':result,'cities':result1,'areas':result2}
    return render(request, 'user/user_edit_profile.html' ,context)

def user_update(request,id):
    id1 = request.user.id
    myfile = request.FILES['uimg']
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
            'user_image' : myfile.name
           }
    User_profile.objects.update_or_create(pk=id,defaults=data)
    data1 = {
            'first_name' : request.POST['fname'],
            'last_name' : request.POST['lname'],
            'username' : request.POST['uname'],
            'email' : request.POST['email']
            }

    user = User.objects.update_or_create(pk=id1,defaults=data1)
    return redirect('/user/user_edit_profile')


def search_worker(request):
    cate_id = request.POST['scate']
    subcate_id = request.POST['subcate']
    result = Worker_profile.objects.filter(category_id=cate_id,subcategory_id=subcate_id)
    context = {'result': result}
    return render(request,'user/search_worker.html',context)
    
def view_worker_details(request,id):
    result = Worker_profile.objects.get(pk=id)
    context = {'worker':result}
    return render(request,'user/view_worker_details.html', context)

def changepass(request):
    context = {}
    return render(request, 'user/changepass.html' ,context)

def changepass_update(request):
    username = request.user.username
    old_password  = request.POST['old_password']
    new_password  = request.POST['new_password']
    rnew_password = request.POST['rnew_password']

    if new_password == rnew_password:
        user = auth.authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password Updated Successfully')
            return redirect('/user/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/user/changepass')     
    else:
         messages.success(request, 'Miss Match Password')

def feedback(request):
    user_id = request.user.id
    result = User_profile.objects.get(user_id=user_id)
    context = {'result':result}
    return render(request, 'user/feedback.html', context)

def feedback_store(request):
    rating = request.POST['rating']
    comment = request.POST['comment']
    id = request.user.id

    Feedback.objects.create(rating=rating, comment = comment, user_id=id)
    messages.success(request,'Thank You For Your Valuable Feedback')

    return redirect('/user/feedback')

def contact(request):
    context = {}
    return render(request, 'user/contact.html', context)

def contact_store(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    contact_cat = request.POST['cat']
    message = request.POST['message']

    Contact_us.objects.create(name=name, email = email,contact=contact,contact_category=contact_cat,message=message)
    messages.success(request,'Thank You for sharing this with us,we will reply by email as soon as possible')

    return redirect('/user/contact')

def post_problem(request):
    result1 = Category.objects.all()
    result2 = Sub_category.objects.all()
    result3 = City.objects.all()
    result4 = Area.objects.all()
    user_id = request.user.id
    result = User_profile.objects.get(user_id=user_id)
    context = {'categories':result1, 'sub_categories':result2,'cities':result3,'areas':result4,'result':result}
    return render(request, 'user/post_problem.html' ,context)

def post_problem_store(request):
    category = request.POST['categoryname']
    subcategory = request.POST['subcategoryname']
    subject = request.POST['subject']
    description = request.POST['pdesc']

    problemfile = request.FILES['pimg']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(problemfile.name,problemfile)

    address = request.POST['address']
    city = request.POST['cityname']
    area = request.POST['areaname']
    id = request.user.id

    Post_problem.objects.create(category_id = category,subcategory_id=subcategory,subject=subject,problem_description = description, problem_image=problemfile,address=address,city_id=city,area_id=area,user_id = id)
    messages.success(request,'Successfully Post Your Problem worker will contect you soon!')
    return redirect('/user/post_problem')

def all_requests(request):
    user_id = request.user.id
    result1 = User_profile.objects.get(user_id=user_id)
    result = Post_problem.objects.filter(user_id=user_id)
    context = {'requests':result,'result1':result1}
    return render(request, 'user/all_requests.html' ,context)


def view_my_request(request,id):
    user_id = request.user.id
    result1 = User_profile.objects.get(user_id=user_id)
    result = Post_problem.objects.get(pk=id)
    context = {'requests':result,'result1':result1}
    return render(request,'user/view_my_request.html', context)

def post_problem_delete(request,id):
    result = Post_problem.objects.get(pk=id)
    result.delete()
    return redirect('/user/all_requests')

def request_edit(request,id):
    result = Post_problem.objects.get(pk=id)
    result1 = Category.objects.all()
    result2 = Sub_category.objects.all()
    result3 = City.objects.all()
    result4 = Area.objects.all()
    user_id = request.user.id
    result5 = User_profile.objects.get(user_id=user_id)
    context = {'result':result,'categories':result1,'sub_categories':result2,'cities':result3,'areas':result4,'result5':result5}
    return render(request, 'user/request_edit.html', context)

def request_update(request,id):
    problemfile = request.FILES['pimg']
    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(problemfile.name,problemfile)

    data = {
            'category_id' : request.POST['categoryname'],
            'subcategory_id' : request.POST['subcategoryname'],
            'subject' : request.POST['subject'],
            'problem_description' : request.POST['pdesc'],
            'address' : request.POST['address'],
            'city_id' : request.POST['cityname'],
            'area_id' : request.POST['areaname'],
            'problem_image' : problemfile.name
           }

    Post_problem.objects.update_or_create(pk=id, defaults=data)
    return redirect('/user/all_requests')

def applications(request,id):
    user_id = request.user.id
    result1 = User_profile.objects.get(user_id=user_id)
    result = Apply_request.objects.filter(user_post_id=id)
    context = {'result':result,'result1':result1}
    return render(request,'user/applications.html',context)

def applications_delete(request,id):
    result = Apply_request.objects.filter(pk=id)
    result.delete()
    return redirect('/user/all_requests')


def hire(request,id,worker_id):
    user_id = request.user.id
    result = User_profile.objects.get(user_id=user_id)
    result1 = Post_problem.objects.get(pk=id)
    context = {'result':result,'result1':result1,'post_id':id,'worker_id':worker_id}
    return render(request, 'user/hire.html', context)

def hire_store(request):
    status = request.POST['status']
    description = request.POST['desc']
    worker_id = request.POST['worker_id']
    post_id = request.POST['post_id']
    id = request.user.id

    Hire.objects.create(status=status, description = description, worker_id=worker_id, user_post_id = post_id, user_id=id)
    # messages.success(request,'Successfully Hire')
    request.session['w_id'] = worker_id
    return redirect('/user/history')
    

def history(request):
    user_id = request.user.id
    result3 = User_profile.objects.get(user_id=user_id)
    result = Hire.objects.filter(user_id=user_id,status='accept')
    
    context = {'result': result,'result3':result3}
    return render(request, 'user/history.html',context)


def all_electricians(request):
    result = Worker_profile.objects.filter(category_id = 1)
    context = {'result': result}
    print(result)
    return render(request,'user/all_electricians.html',context)
    

def all_plumbers(request):
    result = Worker_profile.objects.filter(category_id = 2)
    context = {'result': result}
    return render(request,'user/all_plumbers.html',context)


def all_carpenters(request):
    result = Worker_profile.objects.filter(category_id = 3)
    context = {'result': result}
    return render(request,'user/all_carpenters.html',context)

def all_painters(request):
    result = Worker_profile.objects.filter(category_id = 4)
    context = {'result': result}
    return render(request,'user/all_painters.html',context)
    
    
