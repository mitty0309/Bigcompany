"""firstproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from main.views import bigcompany

from account import views as aviews

from flower import views as fviews
from intro import views as iviews
from product import views as pviews
#from contact import views as conviews
from store import views as sviews

from news import views as nviews
from boardapp import views as bviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', bigcompany),

  # account
  path('login/', aviews.login),
  path('logout/', aviews.logout),
  path('mypage/', aviews.mypage),
  path('register/', aviews.register),

  # news
  path('newsindex/', nviews.index),
  path('newsindex/<str:pageindex>/', nviews.index),
  path('newsdetail/<int:detailid>/', nviews.detail),
  path('newslogin/', nviews.login),
  path('newslogout/', nviews.logout),
  path('newsadminmain/', nviews.adminmain),
  path('newsadminmain/<str:pageindex>/', nviews.adminmain),
  path('newsadd/', nviews.newsadd),
  path('newsedit/<int:newsid>/', nviews.newsedit),
  path('newsedit/<int:newsid>/<str:edittype>/', nviews.newsedit),
  path('newsdelete/<int:newsid>/', nviews.newsdelete),
  path('newsdelete/<int:newsid>/<str:deletetype>/', nviews.newsdelete),

  #boardapp
  path('showpost/', bviews.showpost),
  path('showpost/<str:pageindex>/', bviews.showpost),
  path('addpost/', bviews.addpost),
  path('captcha/', include('captcha.urls')),

# contact
  #path('contact/', conviews.contact),
  #path('contact/create/', conviews.create, name='create'),
  #path('contact/edit/<int:pk>/', conviews.edit, name='edit'),
  #path('contact/delete/<int:pk>/', conviews.delete, name='delete'),
  #path('contact/<slug:slug>/', conviews.detail, name='detail'),

  #intro
  path('intro/', iviews.intro),
  path('intro/create/', iviews.icreate, name='create'),
  path('intro/edit/<int:pk>/', iviews.iedit, name='edit'),
  path('intro/delete/<int:pk>/', iviews.idelete, name='delete'),
  path('intro/<slug:slug>/', iviews.idetail, name='detail'),
# store
  path('store/', sviews.stores),
  path('store/create/', sviews.screate, name='create'),
  path('store/edit/<int:pk>/', sviews.sedit, name='edit'),
  path('store/delete/<int:pk>/', sviews.sdelete, name='delete'),
  path('store/<slug:slug>/', sviews.sdetail, name='detail'),
# product
  path('product/', pviews.product),
  path('product/create/', pviews.pcreate, name='create'),
  path('product/edit/<int:pk>/', pviews.pedit, name='edit'),
  path('product/delete/<int:pk>/', pviews.pdelete, name='delete'),
  path('product/<slug:slug>/', pviews.pdetail, name='detail'),
# flower(放最後面)
  path('flower/', fviews.flowers),
  path('flower/create/', fviews.create, name='create'),
  path('flower/edit/<int:pk>/', fviews.edit, name='edit'),
  path('flower/delete/<int:pk>/', fviews.delete, name='delete'),
  path('flower/<slug:slug>/', fviews.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
