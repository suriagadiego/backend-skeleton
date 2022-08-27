from django.urls import path, include
from . import views as api_home_views
from products import views as products_views
from rest_framework import routers

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
# router.register('home', api_home_views.api_home)
urlpatterns = [
    # path('home', api_home_views.api_home),
    path('', include(router.urls))
    # patch('', views)
]