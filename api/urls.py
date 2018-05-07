from django.urls import include, path
from rest_framework import routers
from apps.bills.views import BillsViewSet
from apps.categorys.views import CategorysViewSet
from apps.users.views import UsersViewSet

router = routers.DefaultRouter()
router.register(r'bills', BillsViewSet)
router.register(r'categorys', CategorysViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('rest_auth/', include('rest_auth.urls')),
]