from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy

from .forms import RegisterForm
# Create your views here.


class CustomLoginView(auth_views.LoginView):
    # LOGIN_REDIRECT_URL is set to homepage in settings.py
    template_name = 'accounts/user_form.html'
    extra_context = {'title_message': 'Login'}
    redirect_authenticated_user = True  # if a user is already logged in, don't show the form ,just redirect


class CustomLogoutView(auth_views.LogoutView):
    next_page = 'accounts:login'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/user_form.html'
    extra_context = {'title_message': 'Register'}
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        user = User.objects.create_user(new_user.username, new_user.email, new_user.password)
        user.first_name = new_user.first_name
        user.last_name = new_user.last_name
        user.save()

        user_to_login = authenticate(username=new_user.username,
                                     password=new_user.password)
        login(self.request, user_to_login)
        return super(RegisterView, self).form_valid(form)

#
# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             newuser = form.save(commit=False)
#             user = User.objects.create_user(newuser.username, newuser.email, newuser.password)
#             user.first_name = newuser.first_name
#             user.last_name = newuser.last_name
#             user.save()
#
#             user_to_login = authenticate(username=newuser.username,
#                                          password=newuser.password)
#             login(request, user_to_login)
#             return redirect('homepage')
#
#     else:
#         form = RegisterForm(None)
#
#     return render(request, 'accounts/user_form.html', {
#         'form': form,
#         'title_message': 'Register'
#     })