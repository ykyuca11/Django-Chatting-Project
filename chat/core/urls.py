from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.sendMessage, name="contacts"),
    path('contacts/', views.contacts, name="friends"),
    path('<int:id>', views.softDelete, name="softdelete"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('reply/', views.reply_message, name="reply"),
    path('readStatus/<int:id>/', views.update_read_status, name='update_read_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)