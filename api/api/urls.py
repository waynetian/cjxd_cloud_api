from django.conf.urls import include, url
from django.contrib import admin

from account import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'organization_info', views.OrganizationInfoViewSet)



urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^user_base_info/?<user_id>', views.UserInfoView.as_view()),


    url(r'^', include(router.urls)),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^orguser/', views.OrgUserView.as_view()),
    url(r'^multi_orguser/', views.MultiOrgUserView.as_view()),




    #url(r'^admin/', include(admin.site.urls)),
]
