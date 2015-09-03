from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	urls(r'^polls/', include('polls.urls', namespace="polls")), 
	urls(r'^admin/', include(admin.site.urls)),
]
