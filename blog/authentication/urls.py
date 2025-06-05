from django.urls import path
from knox import views as knox_view
from authentication.views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_view.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_view.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register/', RegisterView.as_view())
]