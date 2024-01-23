"""
URL configuration for iblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import home, book, packages, services, package, about, signin, signup, activate, signout, profile, add_pass, profile_edit, review

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('signin/', signin),
    path('home/', home),
    path('packages/<slug:url>', package),
    path('about/', about),  
    path('book/', book),
    path('packages/', packages),
    path('services/', services),
    path('signout/', signout),
    path('profile/', profile),
    path('profile-edit/', profile_edit),
    path('add_pass/', add_pass),
    path('review/', review),
    path('activate/<uidb64>/<token>', activate, name="activate")
]
