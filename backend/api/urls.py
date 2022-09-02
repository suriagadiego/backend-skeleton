from django.urls import path, include
from .views import MyTokenObtainPairView
from products import views as products_views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register('users', products_views.UserView)
router.register('brand', products_views.BrandView)
router.register('supplier', products_views.SupplierView)
router.register('job_role', products_views.JobRoleView)
router.register('part_no', products_views.PartNoView)
router.register('transaction_history', products_views.TransactionHistoryView)
router.register('product', products_views.ProductView)
router.register('unit', products_views.UnitView)
router.register('warehouse', products_views.WarehouseView)

urlpatterns = [
    # path('home', api_home_views.api_home),
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # patch('', views)
]