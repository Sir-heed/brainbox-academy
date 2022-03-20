from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('authentication/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def course_list(request):
    template = loader.get_template('authentication/course-list.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def course_grid(request):
    template = loader.get_template('authentication/course-grid.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def course_sidebar(request):
    template = loader.get_template('authentication/course-sidebar.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


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
    context = {
    }
    return HttpResponse(template.render(context, request))


def error(request, exception):
    template = loader.get_template('authentication/error.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def event_details(request):
    template = loader.get_template('authentication/event-details.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def instructor_details(request):
    template = loader.get_template('authentication/instructor-details.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def instructor(request):
    template = loader.get_template('authentication/instructor.html')
    context = {
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
    context = {
    }
    return HttpResponse(template.render(context, request))


def sign_up(request):
    template = loader.get_template('authentication/sign-up.html')
    context = {
    }
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