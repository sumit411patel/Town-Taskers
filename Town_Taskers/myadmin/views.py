from unittest import result
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from myadmin.models import *
from user.models import *
from workers.models import*
from .process import html_to_pdf 
from django.template.loader import render_to_string
from datetime import date
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
	user_count = User_profile.objects.count()
	worker_count = Worker_profile.objects.count()
	order_count = Post_problem.objects.count()
	inquiry = Contact_us.objects.count()
	context = {'u_count':user_count,'w_count':worker_count,'orders':order_count,'inquiries':inquiry}
	return render(request, 'myadmin/dashboard.html' ,context)

def worker_status_approve(request,id):
    data = {'status':'enable'}
    Worker_profile.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_workers')

def worker_status_reject(request,id):
    data = {'status':'disable'}
    Worker_profile.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_workers')

# Category

def add_category(request):
	context = {}
	return render(request, 'myadmin/add_category.html' ,context)

def add_category_store(request):
	mycategory = request.POST['category']

	Category.objects.create(category_name = mycategory)
	return redirect('/myadmin/add_category')

def all_categories(request):
	result = Category.objects.all()
	context = {'categories':result}
	return render(request, 'myadmin/all_categories.html' ,context)

def delete_category(request,id):
	result = Category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_categories')

def edit_category(request,id):
	result = Category.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'myadmin/edit_category.html', context)

def update_category(request,id):
	data = {
			'category_name' : request.POST['category']
	       }

	Category.objects.update_or_create(pk=id, defaults=data)
	return redirect('/myadmin/all_categories')

# Subcategory


def add_sub_category(request):
	result = Category.objects.all()
	context = {'categories':result}
	return render(request, 'myadmin/add_sub_category.html' ,context)

def add_sub_category_store(request):
	mysubcategory = request.POST['subcategory']
	mycategory = request.POST['categoryname']

	Sub_category.objects.create(sub_category_name = mysubcategory, category_id = mycategory )
	return redirect('/myadmin/add_sub_category')

def all_sub_categories(request):
	result = Sub_category.objects.all()
	context = {'sub_categories':result}
	return render(request, 'myadmin/all_sub_categories.html' ,context)

def delete_sub_category(request, id):
	result = Sub_category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_sub_categories')


def edit_sub_category(request, id):
	result1 = Category.objects.all()
	result = Sub_category.objects.get(pk=id)
	context = {'result':result, 'categories': result1}
	return render(request, 'myadmin/edit_sub_category.html', context)

def update_sub_category(request,id):
	data = {
			'sub_category_name' : request.POST['subcategory'],
			'category_id' : request.POST['categoryname']
	       }

	Sub_category.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_sub_categories')


def all_users(request):
	result = User_profile.objects.all()
	context = {'users':result}
	return render(request, 'myadmin/all_users.html' ,context)

def view_all_users(request,id):
	result = User_profile.objects.get(pk=id)
	context = {'users':result}
	return render(request, 'myadmin/view_all_users.html' ,context)


def all_workers(request):
	result = Worker_profile.objects.all()
	context = {'workers':result}
	return render(request, 'myadmin/all_workers.html' ,context)

def view_all_workers(request,id):
	result = Worker_profile.objects.get(pk=id)
	context = {'workers':result}
	return render(request, 'myadmin/view_all_workers.html' ,context)


# City

def add_city(request):
	context = {}
	return render(request, 'myadmin/add_city.html' ,context)

def add_city_store(request):
	mycity = request.POST['city']

	City.objects.create(city_name = mycity)
	return redirect('/myadmin/add_city')

def all_cities(request):
	result = City.objects.all()
	context = {'cities':result}
	return render(request, 'myadmin/all_cities.html' ,context)

def delete_city(request,id):
	result = City.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_cities')

def edit_city(request,id):
	result = City.objects.get(pk=id)
	context = {'result':result}
	return render(request, 'myadmin/edit_city.html', context)

def update_city(request,id):
	data = {
			'city_name' : request.POST['city']
	       }

	City.objects.update_or_create(pk=id, defaults=data)
	return redirect('/myadmin/all_cities')


# Area

def add_area(request):
	result = City.objects.all()
	context = {'cities':result}
	return render(request, 'myadmin/add_area.html' ,context)

def add_area_store(request):
	myarea = request.POST['area']
	mycity = request.POST['cityname']

	Area.objects.create(area_name = myarea, city_id = mycity )
	return redirect('/myadmin/add_area')

def all_areas(request):
	result = Area.objects.all()
	context = {'areas':result}
	return render(request, 'myadmin/all_areas.html' ,context)

def delete_area(request, id):
	result = Area.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/all_areas')


def edit_area(request, id):
	result1 = City.objects.all()
	result = Area.objects.get(pk=id)
	context = {'result':result, 'cities': result1}
	return render(request, 'myadmin/edit_area.html', context)

def update_area(request,id):
	data = {
			'area_name' : request.POST['area'],
			'city_id' : request.POST['cityname']
	       }

	Area.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/all_areas')

# Feedback

def feedback(request):
	result = Feedback.objects.all()
	context = {'feedback':result}
	return render(request, 'myadmin/feedback.html' ,context)

# Inquiry

def inquiry(request):
	result = Contact_us.objects.all()
	context = {'contact':result}
	return render(request, 'myadmin/inquiry.html' ,context)

# Login

def login(request):
	context = {}
	return render(request, 'myadmin/login.html', context)

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']

	result = auth.authenticate(request, username=username,password=password)

	if result is None:
		messages.warning(request,'Invalid Username and Password')
		return redirect('/myadmin')
	else:
		auth.login(request, result)
		return redirect('/myadmin/dashboard')

# Logout

def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login')

# Customer report

def user_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = User_profile.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':User_profile.objects.all()}
    return render(request,'myadmin/user_report.html',context)


# #Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = User_profile.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('tamplates/temp.html', "w").write(render_to_string('customer.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


# Worker report

def worker_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Worker_profile.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'user':result,'f':from_date,'t':to_date} 
        else:
            context = {'user':None} 
    else:
        context = {'user':Worker_profile.objects.all()}
    return render(request,'myadmin/worker_report.html',context)

# #Creating a class based view
class GenerateWorkerPdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Worker_profile.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('tamplates/temp.html', "w").write(render_to_string('worker.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

# Feedback report

def feed_report(request):
    if request.method =='POST':
        from_date = request.POST['from_date']
        to_date   = request.POST['to_date']
        result = Feedback.objects.filter(date__gte=from_date,date__lte=to_date)
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date
        if result.exists():
            context = {'feedback':result,'f':from_date,'t':to_date} 
        else:
            context = {'feedback':None} 
    else:
        context = {'feedback':Feedback.objects.all()}
    return render(request,'myadmin/feedback_report.html',context)

# #Creating a class based view
class GenerateFeedbackPdf(View):
     def get(self, request, *args, **kwargs):
        from_date = request.session['from_date']
        to_date   = request.session['to_date']
        data = Feedback.objects.filter(date__gte=from_date,date__lte=to_date)
        cdate = date.today()
        cdate1 = cdate.strftime('%d/%m/%Y')
        open('tamplates/temp.html', "w").write(render_to_string('feedback.html', {'data': data,'current_date':cdate1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




