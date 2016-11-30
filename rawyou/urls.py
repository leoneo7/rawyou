from django.conf.urls import url, include
from rest_framework.authtoken import views
from django.contrib import admin
from api.urls import router as api_router
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

