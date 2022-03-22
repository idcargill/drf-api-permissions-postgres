from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('duck_blog.urls'), name='home'),
    path('duck/', include('django.contrib.auth.urls')),
    # path('duck/', include('duck_blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
