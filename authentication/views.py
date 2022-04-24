from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import loader

from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .forms import AppointmentForm, LoginForm, TutorCreationForm, UserCreationForm
from .models import Appointment, Tutor, User
from .utils import admin_check

# Create your views here.
def index(request):
    template = loader.get_template('authentication/index.html')
    instructors = Tutor.objects.all()
    context = {
        'instructors':instructors
    }
    return HttpResponse(template.render(context, request))

@login_required()
def course_list(request):
    template = loader.get_template('authentication/course-list.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required()
def course_grid(request):
    template = loader.get_template('authentication/course-grid.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required()
def course_sidebar(request):
    template = loader.get_template('authentication/course-sidebar.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required()
def course_details(request):
    template = loader.get_template('authentication/course-details.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    template = loader.get_template('authentication/blog.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def blog_details(request):
    template = loader.get_template('authentication/blog-details.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('authentication/about.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def cart(request):
    template = loader.get_template('authentication/cart.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def checkout(request):
    template = loader.get_template('authentication/checkout.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    template = loader.get_template('authentication/contact.html')
    context = {}
    form = AppointmentForm(request.POST or None)
    print(form.errors)
    print(form.is_valid())
    if form.is_valid():
        appointment = form.save()
        if request.user.is_authenticated:
            appointment.user = request.user
        appointment.save()
        messages.success(request, "Appointment created successfully.")
        return redirect("authentication:index")
    context['form']= form
    return HttpResponse(template.render(context, request))


def error(request, exception):
    template = loader.get_template('authentication/error.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def instructor_details(request, pk):
    template = loader.get_template('authentication/instructor-details.html')
    user = User.objects.get(id=pk)
    context = {
        'user': user
    }
    return HttpResponse(template.render(context, request))


def instructor(request):
    template = loader.get_template('authentication/instructor.html')
    instructors = Tutor.objects.all()
    context = {
        'instructors': instructors
    }
    return HttpResponse(template.render(context, request))


def product(request):
    template = loader.get_template('authentication/product.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def shop(request):
    template = loader.get_template('authentication/shop.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def sign_in(request):
    template = loader.get_template('authentication/sign-in.html')
    context = {}
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email_or_phone = form.cleaned_data.get('email_or_phone')
        password = form.cleaned_data.get('password')
        try:
            user = User.objects.get(Q(email__iexact=email_or_phone)|Q(phone__iexact=email_or_phone))
            if user.check_password(password):
                next = request.GET.get('next')
                login(request, user)
                messages.success(request, "Login successful.")
                if next is not None:
                    return redirect(next)
                return redirect("authentication:index")
            else:
                messages.error(request,"Incorrect password")
        except User.DoesNotExist:
            messages.error(request,"Invalid email or phone")
    context['form']= form
    return HttpResponse(template.render(context, request))


def sign_up(request):
    template = loader.get_template('authentication/sign-up.html')
    context = {}
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.pop('password')
        user = form.save()
        group, _ = Group.objects.get_or_create(name='student')
        user.groups.add(group)
        user.set_password(password)
        user.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("authentication:index")
    context['form']= form
    return HttpResponse(template.render(context, request))


def site(request):
    template = loader.get_template('authentication/site.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def wishlist(request):
    template = loader.get_template('authentication/wishlist.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(admin_check)
def add_instructor(request):
    template = loader.get_template('authentication/add-instructor.html')
    context = {}
    form = TutorCreationForm(request.POST or None)
    if form.is_valid():
        description = form.cleaned_data.get('description')
        password = form.cleaned_data.pop('password')
        user = form.save()
        group, _ = Group.objects.get_or_create(name='instructor')
        user.groups.add(group)
        user.set_password(password)
        user.save()
        Tutor.objects.create(user=user, description=description)
        messages.success(request, "Tutor created successful.")
        return redirect("authentication:instructor")
    context['form']= form
    return HttpResponse(template.render(context, request))


def user_logout(request):
    logout(request)
    return redirect('authentication:index')


@user_passes_test(admin_check)
def student(request):
    template = loader.get_template('authentication/student.html')
    students = User.objects.filter(groups__name='student')
    paginator = Paginator(students, 10) # Show 25 news per page.
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    context = {
        'students': students
    }
    return HttpResponse(template.render(context, request))


@user_passes_test(admin_check)
def add_instructor(request):
    template = loader.get_template('authentication/add-instructor.html')
    context = {}
    form = TutorCreationForm(request.POST or None)
    if form.is_valid():
        description = form.cleaned_data.get('description')
        password = form.cleaned_data.pop('password')
        user = form.save()
        group, _ = Group.objects.get_or_create(name='instructor')
        user.groups.add(group)
        user.set_password(password)
        user.save()
        Tutor.objects.create(user=user, description=description)
        messages.success(request, "Tutor created successful.")
        return redirect("authentication:instructor")
    context['form']= form
    return HttpResponse(template.render(context, request))


@user_passes_test(admin_check)
def appointment(request):
    template = loader.get_template('authentication/appointment.html')
    appointments = Appointment.objects.all()
    paginator = Paginator(appointments, 10) # Show 25 news per page.
    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)
    context = {
        'appointments': appointments
    }
    return HttpResponse(template.render(context, request))