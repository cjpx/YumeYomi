# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from kanas import views as kana_views
from users import views as user_views
from users_list import views as users_list_view

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

    path('lists/', users_list_view.list_index, name='list_index'),
    path('list/<int:pk>/', users_list_view.list_detail, name='list_detail'),
    path('list/new/', users_list_view.create_list, name='create_list'),
    path('list/<int:list_pk>/add_word/', users_list_view.add_word, name='add_word'),
    path('tags/new/', users_list_view.add_tag, name='add_tag'),
    path('list/<int:pk>/toggle_privacy/', users_list_view.toggle_privacy, name='toggle_privacy'),
    path('like_word_list/', users_list_view.like_word_list, name='like_word_list'),
    path('unlike/<int:pk>/', users_list_view.unlike_word_list, name='unlike_word_list'),
    path('add_tag/', users_list_view.add_tag, name='add_tag'),
    path('word/<int:word_id>/', users_list_view.word_detail, name='word_detail'),
    
    path("", include("learn.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)