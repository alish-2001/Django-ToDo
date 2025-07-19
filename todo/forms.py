from django import forms
from django.core import validators
from ckeditor.widgets import CKEditorWidget

from .models import Task

class TaskForm(forms.ModelForm):

  # description = forms.CharField(widget=CKEditorWidget())

  class Meta:
    model=Task
    fields=['title','description','deadline_datetime',]
    widgets= {
      'deadline_datetime':forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local',}),
      'description':CKEditorWidget(attrs={})
    }   

class NotifyTaskForm(forms.Form):

  task = forms.ModelChoiceField(queryset=None)
  message=forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder':'Your message'}))
  email = forms.EmailField(required=True, validators=[validators.EmailValidator(message="Invalid Email")])


  def __init__(self,user, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["task"].queryset = Task.objects.filter(user=user).all()

  

