from django.urls import include, path
from rest_framework import routers
from budgit.register import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'master-categories', views.MasterCategoryViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'payees', views.PayeeViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
