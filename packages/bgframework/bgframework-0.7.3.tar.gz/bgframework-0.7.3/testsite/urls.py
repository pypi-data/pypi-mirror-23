"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from bgframework.add_ons import get_addons_urls, load_bgframework_addons
from bgframework import views as appviews

load_bgframework_addons()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('bgframework.urls')),
    url(r'', include(get_addons_urls())),
]

if settings.DEBUG:
    urlpatterns += static(settings.ASSETS_URL, document_root=settings.STATIC_ROOT)
