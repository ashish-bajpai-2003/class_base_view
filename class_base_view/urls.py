"""
URL configuration for class_base_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('func/', views.myview , name= 'func'),
    # path('cl/', views.Myview.as_view(),name='cl'),
    # path('subcl/',views.MyviewChild.as_view(),name='subcl'),
    path('homefun/', views.homefun),
    path('cl/', views.HomeClassView.as_view(), name = 'cl'),
    path('contactfun/',views.contactfun, name = 'contactfun'),
    path('contactcl/', views.ContactClassView.as_view(), name = 'contactcl'),
    path('newsfun/',views.newsfun,name= 'newsfun')

]