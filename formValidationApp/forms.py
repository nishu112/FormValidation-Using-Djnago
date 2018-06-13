from django.forms import ModelForm
from django import forms
from formValidationApp.models import *


class PostForm(ModelForm):#define the class of a form
	class Meta:
		model=Post        #write the name of models for which we want the form
		fields=["username","gender","text"]
		#here we can write the custom fields of model or we can select some fields from
		#models which we want show in the form

	def clean(self):
		super(PostForm, self).clean()
		#we get the data of form using super function
		username= self.cleaned_data.get('username')
		text= self.cleaned_data.get('text')
		#extract the username and text field fom the data
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['text'] = self.error_class([
				'Post Should Contain minimum 10 characters'])

		#return any erros if we find any
		return self.cleaned_data
