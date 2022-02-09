from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('inbox/', views.helpdesk_inbox, name='inbox'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     print(urlpatterns)