from rest_framework import routers

from . import views


router = routers.DefaultRouter()

# VRFs
router.register(r'vrfs', views.VRFViewSet)

# RIRs
router.register(r'rirs', views.RIRViewSet)

# Aggregates
router.register(r'aggregates', views.AggregateViewSet)

# Prefixes
router.register(r'roles', views.RoleViewSet)
router.register(r'prefixes', views.PrefixViewSet)

# IP addresses
router.register(r'ip-addresses', views.IPAddressViewSet)

# VLANs
router.register(r'vlan-groups', views.VLANGroupViewSet)
router.register(r'vlans', views.VLANViewSet)

# Services
router.register(r'services', views.ServiceViewSet)

urlpatterns = router.urls
