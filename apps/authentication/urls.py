from django.urls import path
# from .views import login_view, register_user
from apps.authentication import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
# from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('helpdesk/', views.help_form, name="helpdesk"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='accounts/change_password.html'), name="password"),
    path('password_success', views.password_success, name='password_success'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# print('urlpattern',urlpatterns)
# print('static', static)
