from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

# for hosting
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('discord.urls')),
    path('developers/', include('user.urls')),
    path('project/', include('project.urls')),
    path('api/', include('api.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="user/reset_password.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='user/reset_password_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/reset.html'),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="user/reset_password_complete.html"),name="password_reset_complete"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)