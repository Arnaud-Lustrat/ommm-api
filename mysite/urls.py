#from django.conf.urls import url, include
from django.conf.urls import *
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    url(r'', include('ommm.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += patterns('',
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
#)