from django.contrib import admin
from django.urls import path, include

from website.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('albums/', include('albums.urls'))
]
