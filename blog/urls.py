from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, create_post, post_list, post_detail, edit_post, delete_post

from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', home, name='home_page'),
    path('post/new/', create_post, name='create_post'),
    path('post/', post_list, name='post_list'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('post/<int:id>/edit', edit_post, name='post_edit'),
    path('post/<int:id>/delete', delete_post, name='delete_post'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include(router.urls))
]
