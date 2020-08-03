from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, UpdateView

from .models import StudentInformation
from .forms import StudentInfo


def home(request):
    qs = StudentInformation.objects.all()

    context = {
            'qs': qs
    }
    return render(request, 'studentinfo.html', context)


class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = StudentInfo
    success_url = '/'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentInfo
    login_url = '/login/'
    template_name = 'detail-update.html'
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().first_name
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return StudentInformation.objects.all()


@login_required
def delete(request, pk):
    student = StudentInformation.objects.get(id=pk)
    student.delete()
    messages.error(request, 'Student was deleted successfully!')

    return redirect('/')

