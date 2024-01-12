from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='account-home'),
    path('register/', views.register, name='user-register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', ), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='user-logout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)