from django.urls import path
from posts.views import PostView, TagView, AuthorView, PostDetailView, TagDetailView, AuthorDetailView

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('tags/', TagView.as_view()), # projenin ana url kısmında posts olarak buranın url'sini kaydettiğimiz için tags gibi kısımlara girerken /posts/tags eklemek gerekir
    path('<int:pk>/', TagDetailView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('<int:pk>/', AuthorDetailView.as_view())
]