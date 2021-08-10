from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from authentication.authentication import ExpiringTokenAuthentication


class Authentication(object):
    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
                print(token)
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user, token, message = token_expire.authenticate_credentials(token)
            if user is not None and token is not None:
                return user
            return message
        return None

    def dispatch(self, request, *args, **kwargs):
        response = Response({})
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        user = self.get_user(request)
        if user is not None:
            if type(user) == str:
                response = Response({'error': user})
                return response
            return super().dispatch(request, *args, **kwargs)
        response = Response({'error': 'No se han enviado las credenciales necesarias'})
        return response
