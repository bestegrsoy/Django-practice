from django.urls import path, include
from posts.views import AuthorViewSet, TagViewSet, PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet),
router.register('authors', AuthorViewSet),
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]



# urlpatterns = [
#     path('', PostView.as_view()),
#     path('<int:pk>/', PostDetailView.as_view()),
#     path('tags/', TagView.as_view()), # projenin ana url kısmında posts olarak buranın url'sini kaydettiğimiz için tags gibi kısımlara girerken /posts/tags eklemek gerekir
#     path('<int:pk>/', TagDetailView.as_view()),
#     path('authors/', AuthorView.as_view()),
#     path('<int:pk>/', AuthorDetailView.as_view())
# ]