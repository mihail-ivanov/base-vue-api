
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import RefreshJSONWebToken


class ObtainJSONWebTokenByEmail(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        if 'email' in request.data:
            try:
                user = User.objects.get(email=request.data['email'])
            except User.DoesNotExist:
                user = None

            if user:
                del request.data['email']
                request.data['username'] = user.username

        return super().post(request, *args, **kwargs)


class RefreshJSONWebTokenWith201(RefreshJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 400:
            return Response({'status': 'nok'})
        return response


obtain_jwt_token_by_email = ObtainJSONWebTokenByEmail.as_view()
refresh_jwt_token = RefreshJSONWebTokenWith201.as_view()
