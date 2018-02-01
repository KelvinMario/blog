from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.BlogView.as_view(),name='blog'),
    # url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(),name='tag'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    # path('search',views.search,name='search')
    # url(r'^search/$',views.search,name='search')
]