from django.urls import path

from . import views

urlpatterns = [
    path('users',views.filrebaseusers,name="filrebaseusers"),
    path('user/delete/<str:uid>',views.deleteusers,name="deleteusers"),
    path('user/posts/',views.userposts,name="userposts"),
    path('user/post-details/<str:post_id>',views.postview,name="postview"),
    path('user/post-delete/',views.postdelete,name="postdelete"),
    # category
    path('categories/',views.category,name="category"),
    path('category/save/',views.categorysave,name="categorysave"),
    path('category/update/',views.updatecategory,name="updatecategory"),
    path('category/delete/',views.deletecategory,name="deletecategory"),
    # video report
     path('video/reports',views.videoreport,name="videoreport"),


]