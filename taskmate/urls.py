
from django.contrib import admin
from django.urls import path, include
from dolist import views as dolsit_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dolsit_views.index, name="index"),
    path('dolist/', include('dolist.urls')),
    path('account/', include('users_app.urls')),
    path('contact',dolsit_views.contact, name="contact"),
    path('about',dolsit_views.about,name="about"),
]
