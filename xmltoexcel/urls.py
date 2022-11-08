from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

app_name = 'xmltoexcel'
urlpatterns =[
    path('converter/', views.index, name='conversor'),
    path('converternfe/', views.nfe, name='conversornfe'),
    path('convertercte/', views.cte, name='conversorcte'),
    path('converternfscxs/', views.nfscxs, name='conversornfscxs'),



]