from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.state import User
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from django.db import close_old_connections
from urllib.parse import parse_qs
from jwt import decode as jwt_decode
from django.conf import settings
@database_sync_to_async
def get_user(validated_token):
    try:
        user = get_user_model().objects.get(id=validated_token["user_id"])
        # get_user_model will return the project's User model as specified in settings.py
        # from the AUTH_USER_MODEL constant. if none is provided, get_user_model will
        # return the default django user model.
        print(f"{user}")
        return user

    except User.DoesNotExist:
        return AnonymousUser()



class JwtAuthMiddleware(BaseMiddleware):
    """
    Channels middleware that will wraps around the AuthMiddlewareStack as provided by channels.
    Users will have to provide the token as a URL argument
    ws://localhost:8000/ws/chat/?token=<TOKEN>
    """
    def __init__(self, inner):
        self.inner = inner
    async def __call__(self, scope, receive, send):
        close_old_connections() # all timed out database functions are terminated
        # grab the token from the url
        token = parse_qs(scope["query_string"].decode("utf8"))["token"][0] 
        try:
            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            return None
        else:
            # decode the token, and provide the respective user within the consumer's scope object.
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            scope["user"] = await get_user(validated_token=decoded_data)
        return await super().__call__(scope, receive, send)
def JwtAuthMiddlewareStack(inner):
    return JwtAuthMiddleware(AuthMiddlewareStack(inner))