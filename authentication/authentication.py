from datetime import timedelta

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from auth_em.settings import TOKEN_EXPIRED_AFTER_SECONDS


class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        return timedelta(seconds= TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)
        return is_expire, token

    def authenticate_credentials(self, key):
        message, user, token = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token inválido'

        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'

            is_expired = self.token_expire_handler(token)
            if is_expired:
                message = 'Su token ha expirado'

        return token.user, token, message
