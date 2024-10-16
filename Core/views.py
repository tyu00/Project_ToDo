from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
