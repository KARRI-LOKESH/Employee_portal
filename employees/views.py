from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('employee_search')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_search')
    else:
        form = EmployeeForm()
    return render(request, 'employee_add.html', {'form': form})


def employee_search(request):
    query = Employee.objects.all()
    filters = {
        'employee_id': request.GET.get('employee_id', ''),
        'first_name__icontains': request.GET.get('first_name', ''),
        'last_name__icontains': request.GET.get('last_name', ''),
        'login_id__icontains': request.GET.get('login_id', ''),
        'department': request.GET.get('department', ''),
    }
    for key, val in filters.items():
        if val:
            query = query.filter(**{key: val})

    dob_start = request.GET.get('dob_start')
    dob_end = request.GET.get('dob_end')
    if dob_start and dob_end:
        query = query.filter(date_of_birth__range=[dob_start, dob_end])

    paginator = Paginator(query, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee_search.html', {'page_obj': page_obj})


def employee_view(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'emp': emp})


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form, 'employee': employee})


def employee_delete(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    emp.delete()
    return redirect('employee_search')
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})
@require_POST
def employee_bulk_delete(request):
    ids = request.POST.getlist('selected_employees')
    Employee.objects.filter(id__in=ids).delete()
    return redirect('employee_search')
def employee_history(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    history_records = []  
    
    return render(request, 'employee_history.html', {
        'employee': employee,
        'history_records': history_records,
    })