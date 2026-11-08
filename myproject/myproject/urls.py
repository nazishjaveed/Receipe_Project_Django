from django.contrib import admin
from django.urls import path

from home.views import *
from receipe.views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('', home, name='home'),

    path('secondary-page/', secondary_page, name='success_page'),

    path('contact/', contact, name='contact'),

    path('about/', aboutus, name='about'),

    path('receipe/', receipe, name='receipe'),

    path('delete_receipe/<int:id>/', delete_recipe, name='delete_recipe'),

    path('update_receipe/<int:id>/', update_recipe, name='update_recipe'),

    path('login/', login_page, name='login'),

    path('register/', register, name='register'),

    path('logout/', logout_page, name="logout"),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

urlpatterns += staticfiles_urlpatterns()