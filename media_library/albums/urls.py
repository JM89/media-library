from django.urls import path

from .views import list_albums, view_album, create_album

urlpatterns = [
    path('<int:id>', view_album, name="view_album"),
    path('', list_albums, name="list_albums"),
    path('new', create_album, name="new_album")
]
