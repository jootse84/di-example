from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^image2', hello.views.image2, name='image1'),
    url(r'^image1', hello.views.image1, name='image2'),
    url(r'^admin/', include(admin.site.urls)),
]
