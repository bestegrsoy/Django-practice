from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from rest_framework import views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import login



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
    

class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,) # settingsde verdiğimiz permission class'dan register'ın etkilenmesini 
    # istemediğim için yani buraya kimlik doğrulaması olmadan herkes için ulaşılabilir bir endpoint haline getirdik

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token":AuthToken.objects.create(user)[1]
        })