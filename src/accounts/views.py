from django.contrib.auth import views as auth_views

# Create your views here.


class CustomLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(auth_views.LogoutView):
    pass
