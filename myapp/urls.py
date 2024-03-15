from django.conf import settings
from django.urls import path, include
from .views import apply, career_page, home, aboutus, contactus, privacypolicy, service, submit_application, terms_conditions
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('apply/', apply, name='apply'),
    path('career_page/', career_page, name='career_page'),
    path('contactus/', contactus, name='contactus'),
    path('service/', service, name='services'),
    path('terms_conditions/', terms_conditions, name='terms_conditions'),
    path('privacypolicy/', privacypolicy, name='privacypolicy'),
    path('submit_application/', submit_application, name='submit_application'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
