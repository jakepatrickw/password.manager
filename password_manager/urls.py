from re import template
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from password_storage import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.ListPassword.as_view(), name='ListPasswords'),
    path('create/', views.CreatePassword.as_view(), name='CreatePassword'),
    path('delete/<int:id>/', views.DeletePassword.as_view(), name='DeletePassword'),
    path('update/<int:id>/', views.UpdatePassword.as_view(), name='UpdatePassword'),
    path('html/<int:pk>', views.pass_lister, name='PassLister'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='home'),
    path('signup/', views.signup, name='signup'),
]
