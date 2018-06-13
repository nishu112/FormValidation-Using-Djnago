from django.db import models

# Create your models here.
class Post(models.Model):
	Male = 'M'
	FeMale = 'F'
	GENDER_CHOICES = (
	(Male, 'Male'),
	(FeMale, 'Female'),
	)
	username = models.CharField( max_length=20,blank=False,null=False)
	#define a username filed with bound  max length it can have
	text = models.TextField(blank=False, null=False)
	#we'll use this to write a post
	gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default=Male)
	# we are restricting the values of gender by giving it some choices
	time = models.DateTimeField(auto_now_add=True)
	#we don't need to do anythinf for this.whenever we insert anything
	#then it'll automatically save the time for that
