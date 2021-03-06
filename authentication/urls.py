from django.urls import path, include
from django.conf.urls import handler404, handler500
from .views import index, course_list, course_grid, course_sidebar, course_details, blog, blog_details, about, cart, checkout, contact, error, \
    instructor_details, instructor, product, shop, sign_in, sign_up, site, wishlist, add_instructor, user_logout, student, appointment

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('course-list', course_list, name='course-list'),
    path('course-grid', course_grid, name='course-grid'),
    path('course-sidebar', course_sidebar, name='course-sidebar'),
    path('course-details', course_details, name='course-details'),
    path('blog', blog, name='blog'),
    path('blog-details', blog_details, name='blog-details'),
    path('about', about, name='about'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('error', error, name='error'),
    path('instructor-details/<int:pk>', instructor_details, name='instructor-details'),
    path('instructor', instructor, name='instructor'),
    path('product', product, name='product'),
    path('shop', shop, name='shop'),
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('site', site, name='site'),
    path('wishlist', wishlist, name='wishlist'),
    path('add-instructor', add_instructor, name='add-instructor'),
    path('logout', user_logout, name='logout'),
    path('student', student, name='student'),
    path('appointment', appointment, name='appointment'),
]

handler404 = error