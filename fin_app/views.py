from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import FinancialOrganization
from .serializers import FinancialOrganizationSerializer
from .forms import FinancialOrganizationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm

@permission_required('fin_app.add_financialorganization', raise_exception=True)
def create_financial_organization(request):
    # Только кураторы могут создавать организации, так что здесь дополнительная проверка не требуется
    if request.method == 'POST':
        form = FinancialOrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.curator = request.user  # Присваиваем текущего пользователя как куратора
            organization.save()
            return redirect('home')
    else:
        form = FinancialOrganizationForm()
    return render(request, 'fin_app/organization_form.html', {'form': form})



@permission_required('fin_app.change_financialorganization', raise_exception=True)
def edit_financial_organization(request, pk):
    organization = get_object_or_404(FinancialOrganization, pk=pk)
    # Проверяем, что пользователь либо куратор этой организации, либо ревьюер
    if organization.curator == request.user or request.user.groups.filter(name='Ревьюер').exists():
        if request.method == 'POST':
            form = FinancialOrganizationForm(request.POST, instance=organization)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = FinancialOrganizationForm(instance=organization)
    else:
        return redirect('home')  # Недостаточно прав для редактирования
    return render(request, 'fin_app/organization_form.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Перенаправление на главную страницу после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'fin_app/register.html', {'form': form})



def index(request):
    if request.user.groups.filter(name='Ревьюер').exists():
        organizations = FinancialOrganization.objects.all()
    else:
        organizations = FinancialOrganization.objects.filter(curator=request.user)
    return render(request, 'fin_app/index.html', {'organizations': organizations})



class FinancialOrganizationViewSet(viewsets.ModelViewSet):
    queryset = FinancialOrganization.objects.all()
    serializer_class = FinancialOrganizationSerializer
