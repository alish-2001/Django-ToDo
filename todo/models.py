from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Task(models.Model):

  user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks')

  title=models.CharField(max_length=200, blank=False)

  description=RichTextField(blank=True, null=False)

  is_done=models.BooleanField(default=False)

  deadline_datetime=models.DateTimeField()

  slug = models.SlugField(default="", null=False)
  
  datetime_created=models.DateTimeField(auto_now_add=True)
  datetime_modified=models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('todo:task_detail',  args=[self.id])



    