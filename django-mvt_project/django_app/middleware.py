from django.shortcuts import redirect
from django.urls import reverse

class RedirectUnauthorizedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.already_processed = False

    def __call__(self, request):
        if not self.already_processed:
            if not request.user.is_authenticated:
                self.already_processed = True
                return redirect(reverse('login_user')) 
            
        
        response = self.get_response(request)
        return response