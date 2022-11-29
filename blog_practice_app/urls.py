from . import views
from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'blog_practice_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog'),
    path('blogs/create/', BlogCreate.as_view(), name='blog_create'),
    path('blogs/<int:pk>/update/', BlogUpdate.as_view(), name='blog_update'),
    path('blogs/<int:pk>/delete/', BlogDelete.as_view(), name='blog_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('register/', views.register, name='register'),
]