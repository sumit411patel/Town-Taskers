from django.db import models
from django.contrib.auth.models import User
from datetime import date
from myadmin.models import City,Area,Category,Sub_category

# Create your models here.
class User_profile(models.Model):
	address = models.TextField()
	contact = models.BigIntegerField()
	gender = models.CharField(max_length=10)
	date_of_birth = models.DateField()
	city = models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area = models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	user_image = models.CharField(max_length=255)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'user_profile'



class Feedback(models.Model):
	rating = models.CharField(max_length=20)
	comment = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'feedback'

class Post_problem(models.Model):
	category = models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory = models.ForeignKey(Sub_category,on_delete= models.CASCADE)
	subject = models.CharField(max_length=30)
	problem_description = models.TextField()
	problem_image = models.CharField(max_length=255)
	address = models.TextField()
	city = models.ForeignKey(City,on_delete=models.CASCADE,default='')
	area = models.ForeignKey(Area,on_delete=models.CASCADE,default='')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'post_problem'

class Contact_us(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=100)
	contact = models.BigIntegerField()
	contact_category = models.CharField(max_length=30)
	message = models.TextField()
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'contact_us'

class Hire(models.Model):
	status = models.CharField(max_length=10)
	description = models.TextField()
	worker = models.ForeignKey(User, on_delete=models.CASCADE)
	user_post = models.ForeignKey(Post_problem, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'customer')
	date = models.DateField(default=date.today)

	class Meta:
		db_table = 'hire'
 