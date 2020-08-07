from django.urls import path

from . import views

urlpatterns = [
    path('users',views.filrebaseusers,name="filrebaseusers"),
    path('user/delete/<str:uid>',views.deleteusers,name="deleteusers"),
    path('user/posts/',views.userposts,name="userposts"),
    path('user/post-details/<str:post_id>',views.postview,name="postview"),
]