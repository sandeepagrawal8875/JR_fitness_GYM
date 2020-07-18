from .forms import *
from .models import *
from .decorator import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group
from django.contrib import messages
from .filters import *


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'fact/login.html', context)


def logout_User(request):
    logout(request)
    return redirect('login')


def owner_admin(request):
    return render(request, "fact/admin_page.html")


def client(request):
    client_p = Client.objects.all().order_by('-id')

    myFilter = Client_Filter(request.GET, queryset=client_p)
    client_p = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(client_p, 5)
    try:
        client_obj = paginator.page(page)
    except PageNotAnInteger:
        client_obj = paginator.page(1)
    except EmptyPage:
        client_obj = paginator.page(paginator.num_pages)

    form = Client_form()
    if request.method == 'POST':
        form = Client_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Client_form()
    context = {
        'client_obj': client_obj,
        'form': form,
        'myFilter': myFilter
    }
    return render(request, 'fact/client.html', context)


def staff(request):
    staff_p = Staff.objects.all().order_by('-id')

    myFilter = Client_Filter(request.GET, queryset=staff_p)
    staff_p = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(staff_p, 5)
    try:
        staff_obj = paginator.page(page)
    except PageNotAnInteger:
        staff_obj = paginator.page(1)
    except EmptyPage:
        staff_obj = paginator.page(paginator.num_pages)

    form = Staff_form()
    if request.method == 'POST':
        form = Staff_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Staff_form()
    context = {
        'form': form,
        'myFilter': myFilter,
        'staff_obj': staff_obj,
    }
    return render(request, 'fact/staff.html', context)


def visitor(request):
    visitor_p = Visitor.objects.all().order_by('-id')

    myFilter = Client_Filter(request.GET, queryset=visitor_p)
    visitor_p = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(visitor_p, 5)
    try:
        visitor_obj = paginator.page(page)
    except PageNotAnInteger:
        visitor_obj = paginator.page(1)
    except EmptyPage:
        visitor_obj = paginator.page(paginator.num_pages)

    form = Visitor_form()
    if request.method == 'POST':
        form = Visitor_form(request.POST)
        if form.is_valid():
            form.save()
            form = Visitor_form()
    context = {
        'form': form,
        'myFilter': myFilter,
        'visitor_obj': visitor_obj,
    }
    return render(request, 'fact/visitor.html', context)


def home(request):
    home_obj = Home_pic_moti.objects.all()
    trainer_obj = Trainer.objects.all()
    price_obj = Price.objects.all()
    testimonial_obj = Testimonial.objects.all()
    info_obj = Info.objects.all()
    blog_obj = Blog.objects.all()

    context = {
        'home_obj': home_obj,
        'trainer_obj': trainer_obj,
        'price_obj': price_obj,
        'testimonial_obj': testimonial_obj,
        'blog_obj': blog_obj,
        'info_obj': info_obj
    }
    return render(request, 'fact/home.html', context)


def contact(request):
    contact_obj = Contact_us.objects.all()
    form = Contact_us_form(request.POST or None)
    info_obj = Info.objects.all()
    if form.is_valid():
        form.save()
        form = Contact_us_form()

    context = {
        'form': form,
        'contact_obj': contact_obj,
        'info_obj': info_obj
    }
    return render(request, 'fact/contact.html', context)


def services(request):
    info_obj = Info.objects.all()
    price_obj = Price.objects.all()

    context = {
        'info_obj': info_obj,
        'price_obj': price_obj
    }
    return render(request, 'fact/services.html', context)


def blog(request):
    blog_p = Blog.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(blog_p, 5)
    try:
        blog_obj = paginator.page(page)
    except PageNotAnInteger:
        blog_obj = paginator.page(1)
    except EmptyPage:
        blog_obj = paginator.page(paginator.num_pages)

    info_obj = Info.objects.all()
    form = Blog_form()
    if request.method == 'POST':
        form = Blog_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Blog_form()

    context = {
        'blog_obj': blog_obj,
        'info_obj': info_obj,
        'form': form
    }
    return render(request, 'fact/blog.html', context)


def trainer(request):
    info_obj = Info.objects.all()
    trainer_obj = Trainer.objects.all()
    form = Trainer_form(request.POST, request.FILES)
    if request.method == 'POST':
        form = Trainer_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Trainer_form()

    context = {
        'trainer_obj': trainer_obj,
        'info_obj': info_obj,
        'form': form
    }
    return render(request, 'fact/trainer.html', context)


def achivements(request):
    achi_p = Achivement.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(achi_p, 9)
    try:
        achi_obj = paginator.page(page)
    except PageNotAnInteger:
        achi_obj = paginator.page(1)
    except EmptyPage:
        achi_obj = paginator.page(paginator.num_pages)

    form = Achivement_form()
    if request.method == 'POST':
        form = Achivement_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Achivement_form()
    context = {
        'achi_obj': achi_obj,
        'form': form
    }
    return render(request, 'fact/achivements.html', context)


def equipment_galary(request):
    equp_p = Equipment.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(equp_p, 9)
    try:
        equp_obj = paginator.page(page)
    except PageNotAnInteger:
        equp_obj = paginator.page(1)
    except EmptyPage:
        equp_obj = paginator.page(paginator.num_pages)

    form = Equipment_form()
    if request.method == 'POST':
        form = Equipment_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Equipment_form()
    context = {
        'equp_obj': equp_obj,
        'form': form
    }
    return render(request, 'fact/equipment_galary.html', context)


def calculate_BMI(request):
    return render(request, 'fact/calculate_BMI.html')


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'fact/blog_details.html', {'blog': blog})


def delete_equp(request, pk):
    item = Equipment.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('equipment_galary')
    context = {'item': item}
    return render(request, 'fact/delete.html', context)


def delete_achi(request, pk):
    item = Achivement.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('achivements')
    context = {'item': item}
    return render(request, 'fact/delete_achi.html', context)


def delete_blog(request, pk):
    item = Blog.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('blog')
    context = {'item': item}
    return render(request, 'fact/delete_blog.html', context)


def update_trainer(request, pk):
    trainer = Trainer.objects.get(id=pk)
    form = Trainer_form(instance=trainer)

    if request.method == 'POST':
        form = Trainer_form(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer')

    context = {'form': form}
    return render(request, 'fact/trainer_form.html', context)


def delete_trainer(request, pk):
    item = Trainer.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('trainer')
    context = {'item': item}
    return render(request, 'fact/delete_trainer.html', context)


def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = Client_form(instance=client)

    if request.method == 'POST':
        form = Client_form(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')

    context = {'form': form}
    return render(request, 'fact/update_client.html', context)


def delete_client(request, pk):
    item = Client.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('client')
    context = {'item': item}
    return render(request, 'fact/delete_client.html', context)


def update_staff(request, pk):
    staff = Staff.objects.get(id=pk)
    form = Staff_form(instance=staff)

    if request.method == 'POST':
        form = Staff_form(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff')

    context = {'form': form}
    return render(request, 'fact/update_staff.html', context)


def delete_staff(request, pk):
    item = Staff.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('staff')
    context = {'item': item}
    return render(request, 'fact/delete_staff.html', context)


def delete_visitor(request, pk):
    item = Visitor.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('visitor')
    context = {'item': item}
    return render(request, 'fact/delete_visitor.html', context)
