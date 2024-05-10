from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import FinancialOrganizationViewSet, create_financial_organization, edit_financial_organization
from django.contrib.auth import views as auth_views


router = DefaultRouter()
router.register(r'organizations', FinancialOrganizationViewSet)


urlpatterns = [
    path('home/', views.index, name='home'),
    path('api/', include(router.urls)),
    path('new/', create_financial_organization, name='create_organization'),
    path('edit/<int:pk>/', edit_financial_organization, name='edit_organization'),
    path('login/', auth_views.LoginView.as_view(template_name='fin_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/fin_app/login/'), name='logout'),
    path('register/', views.register, name='register'),


]
