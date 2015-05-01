from django.conf.urls import include, url
from django.contrib import admin

from contact import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user_profile', views.UserProfileViewSet)
router.register(r'user', views.UserViewSet)




urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
