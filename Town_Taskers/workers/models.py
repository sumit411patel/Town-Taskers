from django.db import models
from django.contrib.auth.models import User
from datetime import date
from myadmin.models import Category,Sub_category,City
from user.models import *

# Create your models here.

class Worker_profile(models.Model):
	address = models.TextField()
	contact = models.BigIntegerField()
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	city = models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area = models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(Sub_category,on_delete= models.CASCADE)
	work_description = models.TextField()
	worker_image = models.CharField(max_length=255)
	worker = models.OneToOneField(User, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)
	status = models.CharField(default='disable', max_length=20)

	class Meta:
		db_table = 'worker_profile'

class Apply_request(models.Model):
	application = models.CharField(max_length=20)
	reason = models.TextField()
	worker = models.ForeignKey(User, on_delete=models.CASCADE)
	user_post = models.ForeignKey(Post_problem, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'apply_request' 