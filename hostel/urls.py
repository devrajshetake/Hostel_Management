"""hostel_manag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views
from . views import PostUpdateView
from django.conf.urls.static import static
from hostel_manag import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_user,name="login-page"),
    path('home/',views.home,name="home-page"),
    path('registration/',views.student_registration,name="student_registration"),
    path('visitordetails/',views.visitor_registration,name="visitor_registration"),
    path('facilities/',views.facilities,name="facilities"),
    path('contact_save/',views.saveContactDetails,name="contact_save"),
    path('visitor_save/',views.saveVisitorDetails,name="visitor_save"),
    path('student_save/',views.saveStudentDetails,name="student_save"),
    path('about_us/',views.aboutUs,name="about_us"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('view_profile/<int:user_pk>',views.view_profile,name="view_profile"),
    path('rules/',views.rules,name="rules"),
    # path('student_details/',views.student_details,name="student_details"),
    # path('post/<int:pk>/update',PostUpdateView.as_view(),name="post-update"),
    # path('post/<int:pk>/delete',PostDeleteView.as_view(),name="post-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
