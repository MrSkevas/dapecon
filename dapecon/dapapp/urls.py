from django.urls import path
from . import views
from .views import post_detail

app_name = 'dap'

urlpatterns = [
    path('thankyou', views.thank_you, name='thankyou_page'),
    path('contact/', views.contact_view, name='contact_view1'),
    path('', views.arxiki, name='arxiki'),
    path('istoria/', views.istoria, name='istoria'),
    path('anakinoseis/', views.blogs, name='anakinoseis'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('anakinosi/<slug:slug1>/', views.post_detail1, name='post_detail1'),
    path('ideas/<slug:slug2>/', views.post_detail2, name='post_detail2'),



    ]
