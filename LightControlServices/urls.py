from django.conf.urls import url, patterns, include

from django.contrib import admin
from rest_framework import routers
from LightController.views import LightViewSet, ControllerViewSet
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
router.register(r'lights', LightViewSet)
router.register(r'controllers', ControllerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^led_color.html', 'serve', kwargs={'path': 'led_color.html'})
                       ) # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
