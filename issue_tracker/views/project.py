from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from issue_tracker.forms import ProjectForm, TaskForm, ProjectAddUserForm
from issue_tracker.models import Project, Task


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project

    def get_success_url(self):
        return reverse('index')


class TaskCreateProjectView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/create_task_in_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context

    def form_valid(self, form):
        project_id = self.kwargs['project_id']
        form.instance.project_id = project_id
        return super().form_valid(form)

    def get_success_url(self):
        project_id = self.kwargs['project_id']
        return reverse_lazy('project_detail', args=[project_id])


class ProjectAddUserView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/projects_user_add.html'
    form_class = ProjectAddUserForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save(commit=False)
        user.project = project
        user.save()
        form.save()
        return redirect('project_detail', pk=project.pk)
