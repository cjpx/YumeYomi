# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from kanas import views as kana_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hiragana/', RedirectView.as_view(url='/ひらがな/')),
    path('ひらがな/', kana_views.hiragana, name='hiragana'),
    

    path('katakana/', RedirectView.as_view(url='/カタカナ/')),
    path('カタカナ/', kana_views.katakana, name='katakana'),

    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    
    path("", include("learn.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)