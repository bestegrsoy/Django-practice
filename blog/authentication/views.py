from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken

from rest_framework import views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions, throttling
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import login



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,) # kimlik doğrulaması olmadan erilşilebilirlik
    throttle_classes = (throttling.AnonRateThrottle,) # anon olarak özelliştirme sebebimiz tehlikeli kullanıcıların farklı şifre kombinasyonlaru denemesini minimuma düşürmek 

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data) # giriş bilgileri kontrol ediliyor
        serializer.is_valid(raise_exception=True) # geçerli değilse 400 Bad Request döndürür
        user = serializer.validated_data['user'] # 'user' doğrulanmış kullanıcı nesnesidir
        login(request, user)
        return super(LoginView, self).post(request, format=None) # KnoxLoginView kendi post metodunu çağırarak token üretir
        # format=None format ölçeklendirilebilirliğini arttırır


class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,) # settingsde verdiğimiz permission class'dan register'ın etkilenmesini 
    # istemediğim için yani buraya kimlik doğrulaması olmadan herkes için ulaşılabilir bir endpoint haline getirdik

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print("serializer girldi", serializer)
        serializer.is_valid(raise_exception=True)
        print("is_valid check")
        user = serializer.save()
        print("user oluşturuldu", user)
        return Response({
            "user": UserSerializer(user).data,
            "token":AuthToken.objects.create(user)[1] # [1] token stringini döner 
        })