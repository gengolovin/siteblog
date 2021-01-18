from django.urls import path
from .views import Home, PostsByCategory,GetPost, PostsByTag, Search, BLoginView,profile,BLogoutView

urlpatterns = [
    path('',Home.as_view() , name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('login/', BLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', BLogoutView.as_view(), name='logout'),    
]
