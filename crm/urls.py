"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from core import views
from django.conf.urls import handler404, handler500



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(TemplateView.as_view(template_name="index.html")), name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("login/submit", views.submit_login, name="submit_login"),
    path("customer/", include("customer.urls")),
    path("conversor/", include("xmltoexcel.urls")),
    path("conferencias/", include("conferencia_contabil.urls")),
    path("conferencias/", include("conferencia_fiscal.urls")),
    path("importador/", include("importador.urls")),
]

handler500 = 'importador.views.error_500'
handler404 = 'importador.views.error_404'