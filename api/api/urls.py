from django.conf.urls import include, url
from django.contrib import admin

from account import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'user_profile', views.UserProfileViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'user_base_info', views.UserBaseInfoViewSet)


router.register(r'organization', views.OrganizationViewSet)
router.register(r'organization_info', views.OrganizationInfoViewSet)



#router.register(r'department', views.DepartmentViewSet)
#router.register(r'company', views.CompanyViewSet)





urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^auth/', views.AuthView.as_view()),
    url(r'^user_info/', views.UserInfoView.as_view()),


    #url(r'^password/', views.PasswordView.as_view()),


    url(r'^admin/', include(admin.site.urls)),
]
