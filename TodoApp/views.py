from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from . models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.

# -----------class based -------------

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class Taskdetailedview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']


    def get_success_url(self):
        return reverse_lazy('taskupdate',kwargs={'pk':self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


# -----------function based --------------
def home(request):
    viewTask = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':viewTask})
