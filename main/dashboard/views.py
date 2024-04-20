from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.decorators import login_required
from main.models import User



@login_required(login_url='auth:login') 
def index(request):
    """Dashboard index"""
    staff = models.Staff.objects.all()
    context = {
       'staff':staff
        }
    return render(request, 'dashboard/index.html',context)


@login_required(login_url='auth:login') 
def profile_edit(request):
    """Profile edit"""
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('dashboard:index')
    return render(request, 'dashboard/profile/profile.html')


@login_required(login_url='auth:login') 
def update_password(request):
    """Update password"""
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        password_new = request.POST.get('password_new')
        password_conf = request.POST.get('password_conf')
        if user.check_password(password) and password_new == password_conf:
            user.set_password(password_new)
            user.save()
            return redirect('dashboard:index')


@login_required(login_url='auth:login') 
def staff_create(request):
    """Staff create"""
    if request.method == 'POST':
        models.Staff.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            staff_position=request.POST['staff_position'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            address = request.POST['address'],
            gender = request.POST['gender'],
        
        )
        return redirect('dashboard:staff_list')
    return render(request, 'dashboard/staff/create.html')


@login_required(login_url='auth:login') 
def staff_list(request):
    """Staff list"""
    queryset = models.Staff.objects.all()
    context = {
        'queryset':queryset
        }
    return render(request, 'dashboard/staff/list.html', context)


@login_required(login_url='auth:login') 
def staff_detail(request, id):
    """Staff detail"""
    queryset = models.Staff.objects.get(id=id)
    context = {
        'queryset':queryset
        }
    return render(request, 'dashboard/staff/detail.html', context)


@login_required(login_url='auth:login') 
def staff_update(request, id):
    """Staff update"""
    queryset = models.Staff.objects.get(id=id)
    context = {
        'queryset':queryset
        }
    if request.method == 'POST':
        queryset.first_name = request.POST['first_name']
        queryset.last_name = request.POST['last_name']
        queryset.staff_position=request.POST['staff_position']
        queryset.email = request.POST['email']
        queryset.phone = request.POST['phone']
        queryset.address = request.POST['address']
        queryset.gender = request.POST['gender']
        queryset.save()
        return redirect('dashboard:staff_list')
    return render(request, 'dashboard/staff/update.html', context)  


@login_required(login_url='auth:login') 
def staff_delete(request, id):
    """Staff delete"""
    queryset = models.Staff.objects.get(id=id)
    queryset.delete()
    return redirect('dashboard:staff_list')


def attendance_list(request):
    """Attendance list"""
    queryset = models.Attendance.objects.all()
    staff = models.Staff.objects.all()
    context = {
        'queryset':queryset,
        'staff':staff
        }
    return render(request, 'dashboard/attendance/list.html', context)
