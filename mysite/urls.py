from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    url(r'', include('ommm.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)