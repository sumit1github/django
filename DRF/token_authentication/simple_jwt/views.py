from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    permission_classes = ([IsAuthenticated,])
    
    def post(self, request):
        if not request.data.get('email') or not request.data.get('password'):

            return Response({
                'status': 400,
                'error': [
                    'email and password is needed..',
                ],
            })
        
        print(request.data.get('email'), request.data.get('password'))s
        user = authenticate(
            request,
            email= request.data.get('email'), 
            password= request.data.get('password'),
        )
        print(user)
        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            })
        
        else:
            return Response({
                "status":400,
                "error":[
                    "Login failed ....",
                ]
            })


class LogoutApi(APIView):

    permission_classes = ([IsAuthenticated,])

    def post(self, request):
        refresh = RefreshToken.for_user(request.user)
        return Response({
            "status":200,
            "message":"Logout Done..",
        })