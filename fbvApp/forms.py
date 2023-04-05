from django import forms
from fbvApp.models import Student
from fbvApp.models import Todo
from fbvApp.models import Login

class StudentForm(forms.ModelForm):
   class Meta:
      model=Student
      fields='__all__'


class LoginForm(forms.ModelForm):
   class Meta:
      model=Login
      fields='__all__'
      widgets  =  {'password' : forms.PasswordInput()}
   

class TodoForm(forms.ModelForm):
   class Meta:
      model=Todo
      fields='__all__'
      widgets = {'username': forms.HiddenInput() }