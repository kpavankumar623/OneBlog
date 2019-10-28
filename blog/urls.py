from django.urls import path
from .views import (index, BlogListView, BlogDetailedView , BlogCreateView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    path('',index,name='blog'),
    path('bloglist/',BlogListView.as_view(), name = 'bloglist'),
    path('blogdetail/<int:pk>/',BlogDetailedView.as_view(), name = 'blogdetail'),
    path('blogcreate/',BlogCreateView.as_view(),name = 'blogcreate'),
    path('blogupdate/<int:pk>/',BlogUpdateView.as_view(), name = 'blogupdate'),
    path('blogdelete/<int:pk>/',BlogDeleteView.as_view(), name = 'blogdelete'),
]
