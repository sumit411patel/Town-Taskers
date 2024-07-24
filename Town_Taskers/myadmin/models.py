from django.db import models

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=30)

	class Meta:
		db_table = 'category'

class Sub_category(models.Model):
	sub_category_name = models.CharField(max_length=30)
	category = models.ForeignKey(Category,on_delete = models.CASCADE)

	class Meta:
		db_table = 'sub_category'


class City(models.Model):
	city_name = models.CharField(max_length=30)

	class Meta:
		db_table = 'city'

class Area(models.Model):
	area_name = models.CharField(max_length=30)
	city = models.ForeignKey(City,on_delete = models.CASCADE)

	class Meta:
		db_table = 'area'