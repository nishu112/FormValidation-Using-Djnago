from .models import Post
from .forms import PostForm
from .import views
from django.shortcuts import HttpResponse,render,redirect


def home(request):
	if request.method=='POST':  #check if the request is post then we'll check the valid data
		details=PostForm(request.POST)#we pass the form data to the form class
		if details.is_valid():  #in form class we defined the clean function .if all the data is correct as per clean function it return true
			post=details.save(commit=False)# we temporary made an object if we want to add some of our logic into data then we could do it here before we write data in our database
			post.save()  #finally write changes into database
			return HttpResponse("datasubmitted successfully")#redirect it to some another page indicating data  inserted successfully
		else:
			return render(request,"home.html",{'form':details})  # if details are not valid then we'll redirect it into the same page
	else:
		form=PostForm(None)   #if request is get then we'll create an empty form object and render it into the page
		return render(request, 'home.html', {'form':form})
