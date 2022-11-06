from django.shortcuts import redirect, render
from . models import Task
from . forms import TodoFrom


# Create your views here.
def home(request):
    viewTask = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':viewTask})

# def details(request):
#     task = Task.objects.all()
#     return render(request,'details.html',{'task':task})
def delete(request,taskId):
    task = Task.objects.get(id=taskId)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskId):
    task = Task.objects.get(id=taskId)
    uf = TodoFrom(request.POST or None, instance=task)
    if uf.is_valid():
        uf.save()
        return redirect('/')
    return render(request,'edit.html',{'uf':uf, 'task':task})