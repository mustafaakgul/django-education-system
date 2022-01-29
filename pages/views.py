from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher


def index(request):
    #return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')


def about(request):
    #return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')


def contact(request):
    #return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')


def courses(request):
    #return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')


def teachers(request):
    #return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2] #anasayfa 2 kurs olmasnı istedgnen
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_students'] = User.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        return context

#def index(request):
#    return render(request, 'index.html')

class AboutView(TemplateView):
    template_name = 'about.html'

#def about(request):
#   return render(request, 'about.html')

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact') #ilgili url doner
    success_message = 'We received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
