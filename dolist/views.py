from django.shortcuts import render, redirect
from django.http import HttpResponse
from dolist.models import Task
from dolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def dolist(request):
    if request.method == "POST":
        form=TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manage= request.user
            instance.save()
        messages.success(request,('New Task is Added!'))
        return redirect('dolist')
    else:
        all_tasks=Task.objects.filter(manage=request.user).order_by('id')
        paginator=Paginator(all_tasks,5)
        page=request.GET.get('pg')
        all_tasks=paginator.get_page(page)
        
        return render(request,'dolist.html',{ "all_tasks": all_tasks })

@login_required  
def delete_task(request,task_id):
    task=Task.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed!"))
    
    return redirect('dolist')

@login_required  
def edit_task(request, task_id):
    if request.method == "POST":
        task=Task.objects.get(pk=task_id)
        form=TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
        
        messages.success(request,('Task Edited!'))
        return redirect('dolist')
    else:
        task_obj=Task.objects.get(pk=task_id)
        return render(request,'edit.html',{ "task_obj": task_obj })

@login_required  
def complete_task(request, task_id):
    task=Task.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done=True
        task.save()
    else:
        messages.error(request,("Access Restricted, You Are Not Allowed!"))
    
    return redirect('dolist')

@login_required
def pending_task(request, task_id):
    task=Task.objects.get(pk=task_id)
    task.done=False
    task.save()
    
    return redirect('dolist')


def contact(request):
    context={
        "contact_text":"Welcome to Contact Page"
    }
    return render(request,'contact.html', context)

def index(request):
    context={
        "index_text":"Welcome to Index Page"
    }
    return render(request,'index.html', context)

def about(request):
    context={
        "about_text":"Welcome to About Page"
    }
    return render(request,'about.html', context)