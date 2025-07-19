from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import Task
from .forms import TaskForm,NotifyTaskForm

# Create your views here.

class TaskListView(LoginRequiredMixin,generic.ListView):
  model=Task
  template_name='todo/task_list.html'
  context_object_name='tasks'

  def get_queryset(self) :

    user=get_object_or_404(get_user_model(),id=self.request.user.id)
  
    return Task.objects.filter(user=user).all().order_by('is_done','deadline_datetime')


  def get_context_data(self,**kwargs):
    
    context=super().get_context_data(**kwargs)

    search_input=self.request.GET.get('search_input')
    
    if search_input:

      context['tasks'] = context['tasks'].filter(title__icontains=search_input)
      context['search_input'] = search_input

    return context

class TaskDetailView(LoginRequiredMixin,generic.DetailView):

  model=Task
  template_name='todo/task_detail.html'
  context_object_name='task'


class TaskCreateView(LoginRequiredMixin,generic.CreateView):

  model=Task
  template_name='todo/task_create.html'
  form_class=TaskForm
  success_url=reverse_lazy('todo:task_list')
  
  def form_valid(self, form):

    obj=form.save(commit=False)
    obj.user=self.request.user

    return super().form_valid(form)
  
class TaskUpdateView(LoginRequiredMixin,generic.UpdateView):
  
  model=Task
  template_name='todo/task_create.html'
  form_class=TaskForm
    
class TaskDeleteView(LoginRequiredMixin,generic.DeleteView):


  model=Task
  success_url=reverse_lazy('todo:task_list')
  template_name='todo/task_confirm_delete.html'
  context_object_name='task'

@require_POST
def task_done(request,pk):
  
  task_obj=get_object_or_404(Task, id=pk)

  if request.method == 'POST':

    if task_obj.is_done == True:

      Task.objects.filter(id=id).update(is_done=False)

    else:
      
      Task.objects.filter(id=id).update(is_done=True)

    return redirect('todo:task_list')


@login_required 
def task_notify(request):

  user=get_object_or_404(get_user_model(),id=request.user.id)
  
  task_notify_form=NotifyTaskForm(user)


  if request.method=='POST':

    
    task_notify_form=NotifyTaskForm(user,request.POST)

    if task_notify_form.is_valid():

      task=task_notify_form.cleaned_data['task']
      email_message=task_notify_form.cleaned_data['message']
      email_address=task_notify_form.cleaned_data['email']
      
      subject=f"This is message from ToDo App to notify you about '{task.title}'"

      send_mail(
        subject,
        email_message,
        None,
        [email_address,]

      )
      return render(request,'todo/task_notify.html',{'message':email_message})
    
  

  username=request.user.username

  return render(request,'todo/task_notify.html',context={'form':task_notify_form,'username':username})

  