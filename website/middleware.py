from django.shortcuts import render
from django.urls import resolve
from django.conf import settings

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # اجازه بده مسیرهای استاتیک و مدیا اجرا شوند
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)

        # می‌توانید مسیرهایی که نباید بلاک شوند را مشخص کنید
        allowed_paths = ['/', '/admin/', '/accounts/', '/blog/']
        if any(request.path.startswith(p) for p in allowed_paths):
            return self.get_response(request)

        # مسیرهای دیگر را به صفحه Coming Soon هدایت کن
        return render(request, "coming_soon.html")