from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):

        data = request.data
        username = data.get('username')
        password = data.get('password')
        if data.get('type') == 'register':
            try:
                User.objects.create(username=username, password=password)
                return Response({'msg': 'Successfully created'})
            except Exception as err:
                print(str(err))
                return Response({'err': 'Error occurred'})
        else:
            user = User.objects.get(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=401)

