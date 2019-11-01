from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from blog.urls import router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# $  curl -X POST -d '{"username": "admin","password": "admin@blog"}' -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/auth/token/login/

#   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
#                                  Dload  Upload   Total   Spent    Left  Speed
# 100   106  100    57  100    49    161    138 --:--:-- --:--:-- --:--:--   299{"auth_token":"1a1

