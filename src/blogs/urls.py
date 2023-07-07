from django.urls  import path
from .views import (
    BlogView,
    CreatePostView,
    PostDetailView,
    DeletePostView,
    ListPostView,
    UpdatePostView,
    PostDeleteView
)

app_name = 'Blogs'
urlpatterns = [
    path('base/',BlogView.as_view(template_name='base.html'),name='list-blogs'),
    path('',ListPostView.as_view(),name='list-post'),
    path('create/',CreatePostView.as_view(),name='create-post'),
    path('<int:id>/',PostDetailView.as_view(),name='detail-post'),
    path('<int:id>/update/',UpdatePostView.as_view(),name='update-post'),
    path('<int:id>/delete/',DeletePostView.as_view(),name='delete-post'),
    path('<int:id>/remove/',PostDeleteView.as_view(),name='remove-post'),
]
