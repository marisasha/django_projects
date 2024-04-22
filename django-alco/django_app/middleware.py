from datetime import datetime, timedelta
from typing import Callable

from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse


def logout_on_timeout(get_response: Callable[[HttpRequest], HttpResponse]) -> Callable:
    ttl = settings.LOGOUT_TIMEOUT

    def middleware(request: HttpRequest) -> HttpResponse:
        user = request.user
        user_last_login = user.last_login.replace(tzinfo=None)

        if (
            not user.is_anonymous
            and user_last_login < datetime.now() - timedelta(seconds=ttl)
        ):
            logout(request)

        response = get_response(request)
        return response

    return middleware