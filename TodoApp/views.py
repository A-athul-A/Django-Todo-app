from django.shortcuts import redirect, render
from . models import Task


# Create your views here.
def home(request):
    viewTask = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        task = Task(name=name,priority=priority)
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