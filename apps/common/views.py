from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from apps.common.forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from apps.userprofile.models import Profile
from django.http import HttpResponseRedirect

""" class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html' """

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form=UserForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
             user_form=user_form,
             profile_form=profile_form
             )

        return self.render_to_response(context)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'common/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'

class EventsView(TemplateView):
    template_name = 'common/Events.html'

class WebinarView(TemplateView):
    template_name = 'common/webinar.html'

class NotesView(TemplateView):
    template_name = 'common/notes2.html'

class BookView(TemplateView):
    template_name = 'common/book_now.html'

class CourseView(TemplateView):
    template_name = 'common/course.html'

    