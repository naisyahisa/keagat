from django.urls import path
# from .views import login_view, register_user
from apps.authentication import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('helpdesk/', views.help_form, name="helpdesk")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# print('urlpattern',urlpatterns)
# print('static', static)
