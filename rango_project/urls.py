from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView


# a class to override the default behaviour upon a succesful login
class ModifiedRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/rango/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rango_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('apprango.urls', namespace="apprango")),
    url(r'^accounts/register/$', ModifiedRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, namspace='media')
