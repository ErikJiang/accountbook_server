from django.urls import include, path
from rest_framework import routers
from apps.bills.views import BillsViewSet
from apps.categorys.views import CategorysViewSet
from apps.users.views import UsersViewSet

router = routers.DefaultRouter()
# 若存在自定义get_queryset方法的视图集，则该视图集在注册时需设置base_name
router.register(r'bills', BillsViewSet, base_name='bills')
router.register(r'categorys', CategorysViewSet, base_name='categorys')
router.register(r'users', UsersViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),
]